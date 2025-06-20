# import libraries
import argparse
from pyspark.sql import SparkSession
import re
from subprocess import Popen, PIPE

# extract parameters
parser = argparse.ArgumentParser()
parser.add_argument('--staging_path', type=str)
parser.add_argument('--data_source', type=str)
args = parser.parse_args()
staging_path = args.staging_path
data_source = args.data_source
# staging_path = "/user/hive/warehouse/staging"
# data_source = "product1.public"

# init spark session
spark = (
    SparkSession.builder
    .config("hive.metastore.uris", "thrift://hive-metastore:9083")
    .config("spark.sql.warehouse.dir", "hdfs://namenode:9000/user/hive/warehouse/default")
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
    .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog")
    .enableHiveSupport()
    .getOrCreate()
)

# create new staging tables
pattern = re.compile(rf"{data_source}.*")
p = Popen(f"hdfs dfs -ls {staging_path}/topics", shell=True, stdout=PIPE, stderr=PIPE)
all_paths = [path.decode("utf-8").split()[-1].split("/")[-1] for path in p.stdout][1:]
all_tables = [path for path in all_paths if pattern.match(path)]
for table in all_tables:
    hdfs_path = f"hdfs://namenode:9000{staging_path}/topics/{table}"
    table_name = table.replace(".", "_")
    df = (
        spark.read.format('parquet')
        .options(header=True, inferSchema=True)
        .load(hdfs_path)
    )
    if spark.sql(f"show tables from staging like '{table_name}'").isEmpty():
        print(table_name)
        spark.sql(f"""
            create external table if not exists staging.{table_name}
            ({', '.join([col + ' ' + dtype for col, dtype in df.dtypes])})
            partitioned by (__ds)
            stored as parquet
            location "{hdfs_path}"
        """)
        spark.sql(f'repair table staging.{table_name}')

# create new rawvault tables
table_name_pattern = data_source.replace(".", "_")
staging_table_list = (
    spark.sql(f"show tables from staging like '{table_name_pattern}_*'")
        .select("tableName")
        .rdd.flatMap(lambda x: x).collect()
)
rawvault_table_list = (
    spark.sql(f"show tables from rawvault like '{table_name_pattern}_*'")
        .select("tableName")
        .rdd.flatMap(lambda x: x).collect()
)
new_tables = list(set(staging_table_list) - set(rawvault_table_list))
for table in new_tables:
    tables = {"derived": f"{table}_der", "snapshot": f"{table}_snp", "main": table}
    for table_type, table_name in tables.items():
        print(table_name)
        df = spark.sql(f"select * from staging.{tables['main']}")
        spark.sql(f"""
        create external table if not exists rawvault.{table_name}
        ({', '.join([col + ' ' + dtype for col, dtype in df.dtypes])})
        using iceberg
        {'partitioned by (days(updated_datetime))' if table_type == 'main' else ''}
        location 'hdfs://namenode:9000/user/hive/warehouse/rawvault'
        tblproperties(
            'objcapabilities'='extread,extwrite',
            'engine.hive.enabled'='true',
            'write.delete.mode'='copy-on-write',
            'write.update.mode'='copy-on-write',
            'write.merge.mode'='copy-on-write',
            'external.table.purge'='true',
            'iceberg.file_format'='parquet',
            'format-version'='2',
            'read.parquet.vectorization.batch-size'='10000',
            'read.parquet.vectorization.enabled'='false'
        )
        """)

# run streaming
for staging_table in staging_table_list:
    stream_reader = (
        spark.readStream
        .schema(spark.sql(f"select * from staging.{staging_table}").schema)
        .parquet(f"{staging_path}/topics/{staging_table.replace('_', '.')}")
    )
    stream_query = (
        stream_reader.writeStream
        .outputMode("append").format("iceberg")
        .option("checkpointLocation", f"hdfs://namenode:9000{staging_path}/checkpoints/{staging_table}")
        .trigger(processingTime="10 seconds")
        .toTable(f"rawvault.{staging_table}_der")
    )
spark.streams.awaitAnyTermination()