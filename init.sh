#!/bin/bash

export ICEBERG_LAKEHOUSE_PLATFORM_NETWORK=iceberg_lakehouse_platform

if [[ "$(docker network ls | grep "${ICEBERG_LAKEHOUSE_PLATFORM_NETWORK}")" == "" ]] ; then
    docker network create "${ICEBERG_LAKEHOUSE_PLATFORM_NETWORK}"

else
    echo "Network ${ICEBERG_LAKEHOUSE_PLATFORM_NETWORK} already exists"

fi