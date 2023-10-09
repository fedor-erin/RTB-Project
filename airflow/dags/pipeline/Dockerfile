FROM python:3.8.3

RUN apt-get update -y \
    && apt-get install -y python3-dev python3-pip build-essential \
    && apt-get install gcc -y \
    && apt-get install sudo -y \
    && apt-get clean
RUN adduser --disabled-password --gecos '' airflow
USER airflow

WORKDIR /app
COPY src/ /app/src
COPY requirements.txt /app/
RUN pip install -r requirements.txt
