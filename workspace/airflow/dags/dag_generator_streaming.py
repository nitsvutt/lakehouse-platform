import yaml
import pendulum
from glob import glob
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

TIMEZONE = pendulum.timezone('Asia/Ho_Chi_Minh')

for path in glob("/opt/airflow/configs/streaming/*.yaml"):
    with open(path) as file:
        try:
            CONFIG = yaml.safe_load(file)
        except yaml.YAMLError as exception:
            print(exception)

    default_args = {
        'owner': 'vutt',
        'depends_on_past': False,
        'start_date': datetime(CONFIG["start_date"][0], CONFIG["start_date"][1], CONFIG["start_date"][2], tzinfo=TIMEZONE)
    }
    with DAG(
        dag_id = CONFIG["dag_id"],
        default_args = default_args,
        max_active_runs = 1,
        schedule = CONFIG["schedule"]
    ) as dag:
        spark_submit = SparkSubmitOperator(
            task_id = 'spark_submit',
            conn_id = 'spark_default',
            name = CONFIG["dag_id"],
            application = CONFIG["application"],
            jars = CONFIG["jars"],
            num_executors = CONFIG["num_executors"],
            executor_cores = CONFIG["executor_cores"],
            driver_memory = CONFIG["driver_memory"],
            executor_memory = CONFIG["executor_memory"],
            application_args = [
                "--staging_path", CONFIG["staging_path"],
                "--data_source", CONFIG["data_source"],
            ]
        )
