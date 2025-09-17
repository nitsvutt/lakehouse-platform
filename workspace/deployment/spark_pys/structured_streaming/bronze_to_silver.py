print(f"{'#'*4} - Import libraries")
import argparse
import json
from pyspark.sql import SparkSession
import re

print(f"{'#'*4} - Extract parameters")
parser = argparse.ArgumentParser()
parser.add_argument('--warehouse_path', type=str)
parser.add_argument('--data_source', type=str)
parser.add_argument('--biz_key_map', type=str)
args = parser.parse_args()
warehouse_path = args.warehouse_path
data_source = args.data_source
biz_key_map = json.loads(args.biz_key_map)

print(f"{'#'*4} - Init spark session")
spark = (
    SparkSession.builder
    .config("hive.metastore.uris", "thrift://hive-metastore:9083")
    .config("spark.sql.warehouse.dir", "hdfs:///user/hive/warehouse/default")
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
    .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog")
    .enableHiveSupport()
    .getOrCreate()
)

print(f"{'#'*2} - Create new bronze tables")
pattern = re.compile(rf"{data_source}.*")
hadoop = spark.sparkContext._jvm.org.apache.hadoop
fs = hadoop.fs.FileSystem
conf = hadoop.conf.Configuration() 
path = hadoop.fs.Path(f"{warehouse_path}/bronze/topics")
all_paths = [str(f.getPath()).split("/")[-1] for f in fs.get(conf).listStatus(path)]
all_tables = [path for path in all_paths if pattern.match(path)]
print(f"{'#'*4} - all_tables={all_tables}")
for table in all_tables:
    hdfs_path = f"{warehouse_path}/bronze/topics/{table}"
    table_name = table.replace(".", "_")
    df = (
        spark.read.format('parquet')
        .options(header=True, inferSchema=True)
        .load(hdfs_path)
    )
    if spark.sql(f"show tables from bronze like '{table_name}'").isEmpty():
        print(f"{'#'*4} - Create table bronze.{table_name}")
        spark.sql(f"""
            create external table if not exists bronze.{table_name}
            ({', '.join([col + ' ' + dtype for col, dtype in df.dtypes])})
            partitioned by (__ds)
            stored as parquet
            location "{hdfs_path}"
        """)
        spark.sql(f'repair table bronze.{table_name}')

print(f"{'#'*2} - Create new silver tables")
table_name_pattern = data_source.replace(".", "_")
bronze_table_list = (
    spark.sql(f"show tables from bronze like '{table_name_pattern}_*'")
        .select("tableName")
        .rdd.flatMap(lambda x: x).collect()
)
silver_table_list = (
    spark.sql(f"show tables from silver like '{table_name_pattern}_*'")
        .select("tableName")
        .rdd.flatMap(lambda x: x).collect()
)
new_bronze_tables = list(set(bronze_table_list) - set(silver_table_list))
print(f"{'#'*4} - new_bronze_tables={new_bronze_tables}")
for new_bronze_table in new_bronze_tables:
    table_list = {"derived": f"{new_bronze_table}_der", "snapshot": f"{new_bronze_table}_snp"}
    df = spark.sql(f"select * from bronze.{new_bronze_table}")
    for table_type, table_name in table_list.items():
        print(f"{'#'*4} - Create table silver.{table_name}")
        spark.sql(f"""
            create external table if not exists silver.{table_name}
            ({', '.join([col + ' ' + dtype for col, dtype in df.dtypes])})
            using iceberg
            location '{warehouse_path}/silver/{table_name}'
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
    print(f"{'#'*4} - Create view silver.{new_bronze_table}")
    spark.sql(f"""
        create view if not exists silver.{new_bronze_table} as
        with ranking as (
            select *,
                row_number() over(
                    partition by {', '.join(biz_key_map[new_bronze_table.replace(f'{table_name_pattern}_', '')])}
                    order by __src_ts_ms desc, __lsn desc
                ) as rn
            from silver.{table_list['derived']}
        )
        select *
        from ranking
        where rn = 1 and __op <> 'd'
    """)

print(f"{'#'*2} - Run streaming")
for staging_table in staging_table_list:
    stream_reader = (
        spark.readStream
        .schema(spark.sql(f"select * from staging.{staging_table}").schema)
        .parquet(f"hdfs://{staging_path}/topics/{staging_table.replace('_', '.')}")
    )
    stream_query = (
        stream_reader.writeStream
        .outputMode("append").format("iceberg")
        .option("checkpointLocation", f"hdfs://{staging_path}/checkpoints/{staging_table}")
        .trigger(processingTime="10 seconds")
        .toTable(f"rawvault.{staging_table}_der")
    )
spark.streams.awaitAnyTermination()