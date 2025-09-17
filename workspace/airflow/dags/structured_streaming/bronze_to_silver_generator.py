import yaml
import pendulum
from glob import glob
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

TIMEZONE = pendulum.timezone('Asia/Ho_Chi_Minh')

for path in glob("/opt/airflow/configs/structured_streaming/bronze_to_silver/*.yaml"):
    with open(path) as file:
        try:
            CONFIG = yaml.safe_load(file)
        except yaml.YAMLError as exception:
            print(exception)

    default_args = {
        'owner': CONFIG.get("owner", "vutt"),
        'depends_on_past': CONFIG.get("depends_on_past", True),
        'start_date': datetime(CONFIG["start_date"][0], CONFIG["start_date"][1], CONFIG["start_date"][2], tzinfo=TIMEZONE)
    }
    with DAG(
        dag_id = CONFIG["dag_id"],
        default_args = default_args,
        max_active_runs = CONFIG.get("max_active_runs", 1),
        max_active_tasks = CONFIG.get("max_active_tasks", 1),
        schedule = CONFIG.get("schedule", None),
        catchup = CONFIG.get("catchup", False),
        tags = CONFIG.get("tags", ["need_tags"])
    ) as dag:
        spark_submit = SparkSubmitOperator(
            task_id = 'spark_submit',
            conn_id = CONFIG.get("conn_id", "spark_default"),
            name = CONFIG["dag_id"],
            application = CONFIG["application"],
            jars = CONFIG.get("jars", ""),
            num_executors = CONFIG.get("num_executors", 1),
            executor_cores = CONFIG.get("executor_cores", 3),
            driver_memory = CONFIG.get("driver_memory", "1G"),
            executor_memory = CONFIG.get("executor_memory", "4G"),
            application_args = CONFIG.get("application_args", [])
        )
