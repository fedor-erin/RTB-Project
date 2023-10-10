import os
from datetime import datetime, timedelta
from docker.types import Mount
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.docker_operator import DockerOperator


PROJECT_DIRECTORY = os.environ['PROJECT_DIRECTORY']

default_args = {
    'owner': 'airflow',
    'description': 'RTB pipeline',
    'depend_on_past': False,
    'start_date': datetime(2023, 10, 8),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=10)
}

with DAG('RTB_Predict_Pipeline',
         default_args=default_args,
         schedule_interval="0 * * * *",  # hourly at **:00
         catchup=False) as dag:

    start = BashOperator(
        task_id="start",
        bash_command="echo \"Start of the predicting pipeline! Project directory: '$PROJECT_DIRECTORY'\"",
    )

    docker_operator_params = {
        'image': 'docker_job_image',
        'api_version': 'auto',
        'auto_remove': True,
        'docker_url': "unix://var/run/docker.sock",
        'network_mode': "bridge",
        'mounts': [
            Mount(source=f"{PROJECT_DIRECTORY}/data", target="/app/data", type="bind"),
            Mount(source=f"{PROJECT_DIRECTORY}/models", target="/app/models", type="bind"),
            Mount(source=f"{PROJECT_DIRECTORY}/reports", target="/app/reports", type="bind"),
        ],
    }

    make_test_dataset = DockerOperator(
        **docker_operator_params,
        task_id='make_test_dataset',
        container_name='task___make_test_dataset',
        command="python src/data/make_dataset.py test",
    )

    predict = DockerOperator(
        **docker_operator_params,
        task_id='predict',
        container_name='task___predict',
        command="python src/models/make_predicting.py",
    )

    end = BashOperator(
        task_id="end",
        bash_command="echo \"End of the predicting pipeline!\"",
    )

    start >> make_test_dataset >> predict >> end
