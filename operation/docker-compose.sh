#!/bin/bash

# determine which prompt
if [ $1 == "up" ]; then
    command="docker compose up -d"
elif [ $1 == "down" ]; then
    command="docker compose down"
elif [ $1 == "start" ]; then
    command="docker compose start"
elif [ $1 == "stop" ]; then
    command="docker compose stop"
elif [ $1 == "restart" ]; then
    command="docker compose restart"
else
    echo "ERROR: Invalid prompt $1, must specify: up, down, start, stop, restart"
    exit 1
fi

# remove the first argument
prompt="$1"
shift

# run prompt with specified services
available_services=("product1" "product2" "kafka" "hadoop" "hive" "trino" "airflow")
data_source_services=("product1" "product2")
if [ $1 == "all" ]; then
    echo "INFO: docker compose ${prompt} all services"
    for available_service in ${available_services[@]}; do
        echo "INFO: docker compose ${prompt} ${available_service}"
        if [[  ${data_source_services[@]} =~ ${available_service} ]]; then
            cd "${PROJECT_PATH}/lakehouse-platform/data-source/${available_service}"
        else
            cd "${PROJECT_PATH}/lakehouse-platform/${available_service}"
        fi
        eval ${command}
    done
else
    for request_service in $@; do
        if [[ ${available_services[@]} =~ ${request_service} ]]; then
            for available_service in ${available_services[@]}; do
                if [ ${request_service} == ${available_service} ]; then
                    echo "INFO: docker compose ${prompt} ${request_service}"
                    if [[  ${data_source_services[@]} =~ ${request_service} ]]; then
                        cd "${PROJECT_PATH}/lakehouse-platform/data-source/${request_service}"
                    else
                        cd "${PROJECT_PATH}/lakehouse-platform/${request_service}"
                    fi
                    eval ${command}
                fi
            done
        else
            echo "WARNNING: Undefined service ${request_service}"
        fi
    done
fi