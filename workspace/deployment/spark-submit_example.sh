#!/bin/bash

spark-submit --master yarn \
    --class org.apache.spark.examples.SparkPi \
    --deploy-mode cluster \
    --num-executors 3 \
    --executor-cores 3 \
    --driver-memory 1G \
    --executor-memory 3G \
    /opt/spark/examples/jars/spark-examples_2.12-3.4.1.jar \
    1000