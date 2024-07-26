#!/bin/bash

ICEBERG_LAKEHOUSE_PLATFORM_NETWORK=iceberg_lakehouse_platform

if [[ "$(docker network ls | grep "${ICEBERG_LAKEHOUSE_PLATFORM_NETWORK}")" == "" ]] ; then
    echo "INFO: docker network create ${ICEBERG_LAKEHOUSE_PLATFORM_NETWORK}"
    docker network create "${ICEBERG_LAKEHOUSE_PLATFORM_NETWORK}"
else
    echo "WARNNING: Network ${ICEBERG_LAKEHOUSE_PLATFORM_NETWORK} already exists"
fi