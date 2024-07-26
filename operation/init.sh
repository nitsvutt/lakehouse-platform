#!/bin/bash

DATA_PLATFORM_NETWORK=lakehouse_platform

if [[ "$(docker network ls | grep "${DATA_PLATFORM_NETWORK}")" == "" ]] ; then
    echo "INFO: docker network create ${DATA_PLATFORM_NETWORK}"
    docker network create "${DATA_PLATFORM_NETWORK}"
else
    echo "WARNNING: Network ${DATA_PLATFORM_NETWORK} already exists"
fi