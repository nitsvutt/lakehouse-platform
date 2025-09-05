#!/bin/bash

# clone repo for the first time
if [ -d "./druid" ]; then
    echo "./druid repo does exist."
else
    git clone https://github.com/apache/druid.git
fi

# copy custom file to druid repo
cp -f ./docker-compose.yml ./druid/docker-compose.yml
cp -f ./Dockerfile ./druid/Dockerfile

# run docker compose if you don't perform any customization on Docker image
docker-compose -f ./druid/docker-compose.yml up -d