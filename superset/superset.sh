#!/bin/bash

# clone repo for the first time
if [ -d "./superset" ]; then
    echo "./superset repo does exist."
else
    git clone https://github.com/apache/superset.git
    echo "sqlalchemy-trino" >> ./superset/docker/requirements-local.txt
fi

# run docker compose if you don't perform any customization on Docker image
docker-compose -f ./superset/docker-compose-non-dev.yml up -d

# Trino connection
# trino://trino@trino-coordinator:8080