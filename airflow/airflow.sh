#!bin/sh

# remove old file
rm docker-compose.yaml

# get file
wget -O docker-compose.yaml https://airflow.apache.org/docs/apache-airflow/2.8.2/docker-compose.yaml

# create necessary directories
mkdir -p $COMMON_PATH/airflow/logs $COMMON_PATH/airflow/data

# create an .env file to assign the current user ID
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

# up airflow-init
docker compose up airflow-init

# up all airflow containers
docker compose up -d