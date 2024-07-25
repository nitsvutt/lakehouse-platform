import yaml
import pendulum
from glob import glob
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator

TIMEZONE = pendulum.timezone('Asia/Ho_Chi_Minh')

def _check_some_condictions(dag_id: str):
    print(f"check some condictions for {dag_id}")

for path in glob("/opt/airflow/configs/type_1/*.yaml"):
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
        dag_id=CONFIG["dag_id"],
        default_args=default_args,
        schedule=CONFIG["schedule"]
    ) as dag:
        check_condictions = PythonOperator(
            task_id='check_condictions',
            python_callable=_check_some_condictions,
            op_kwargs={'dag_id': CONFIG["dag_id"]}
        )
        spark_submit = BashOperator(
            task_id='spark_submit',
            bash_command=f'echo spark_submit for {CONFIG["dag_id"]}'
        )
        check_condictions >> spark_submit
