#!/bin/sh
docker compose up airflow-init
docker build -f airflow/dags/pipeline/Dockerfile -t docker_job_image .
docker compose up
