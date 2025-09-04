#!/bin/bash

# clone repo for the first time
if [ -d "./superset" ]; then
    echo "./superset repo does exist."
else
    git clone https://github.com/apache/superset.git
fi

# copy custom file to superset repo
cp -f ./docker-compose-non-dev.yml ./superset/docker-compose-non-dev.yml
cp -f ./.env-local ./superset/docker/.env-local
cp -f ./requirements-local.txt ./superset/docker/requirements-local.txt

# run docker compose if you don't perform any customization on Docker image
docker-compose -f ./superset/docker-compose-non-dev.yml up -d

# Trino connection
# trino://trino@trino-coordinator:8080