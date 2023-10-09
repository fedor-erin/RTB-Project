import os
from datetime import datetime, timedelta
from docker.types import Mount
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.docker_operator import DockerOperator


PROJECT_DIRECTORY = os.environ['PROJECT_DIRECTORY']

default_args = {
    'owner': 'airflow',
    'description': 'ML RTB pipeline',
    'depend_on_past': False,
    'start_date': datetime(2023, 10, 9),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=10)
}

with DAG('ML_RTB_Pipeline',
         default_args=default_args,
         schedule_interval="0 9 * * *",  # daily at 09:00
         catchup=False) as dag:

    start = BashOperator(
        task_id="start",
        bash_command="echo \"Start of a pipeline! Project directory: '$PROJECT_DIRECTORY'\"",
    )

    end = BashOperator(
        task_id="end",
        bash_command="echo \"End of a pipeline!\"",
    )

    test = DockerOperator(
        task_id='test',
        image='docker_job_image',
        container_name='task___test',
        api_version='auto',
        auto_remove=True,
        command=["ls", "-al"],
        mounts=[
            Mount(source=f"{PROJECT_DIRECTORY}/data", target="/app/data", type="bind"),
            Mount(source=f"{PROJECT_DIRECTORY}/models", target="/app/models", type="bind"),
            Mount(source=f"{PROJECT_DIRECTORY}/reports", target="/app/reports", type="bind"),
        ],
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge"
    )

    start >> test >> end
