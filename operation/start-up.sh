#!/bin/bash

if [ $1 == "all" ]; then
    echo "start up all services"

else
    available_services=("kafka" "hadoop" "hive" "spark" "airflow" "gateway")
    for request_service in $@; do
        for available_service in ${available_services[@]}; do
            if [ $request_service == $available_service ]; then
                echo "start up $request_service"
                cd "$PROJECT_PATH/iceberg-lakehouse-platform/$request_service"
                # docker compose up -d
            fi
        done
    done

fi