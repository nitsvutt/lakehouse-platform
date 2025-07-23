#!/bin/bash

if [ "$HADOOP_MODE" = "master" ]; then
    if [ ! -d "/hadoop/dfs/name" ] || [ -z "$(ls -A /hadoop/dfs/name)" ]; then
        echo "Namenode hasn't been formatted yet"
        $HADOOP_HOME/bin/hdfs namenode -format -force
    else
        echo "Namenode has been already formatted"
    fi
    $HADOOP_HOME/bin/hdfs --daemon start namenode
    $HADOOP_HOME/bin/yarn --daemon start resourcemanager
    tail -f /dev/null

elif [ "$HADOOP_MODE" = "worker" ]; then
    if [ ! -d "/hadoop/dfs/name" ] || [ -z "$(ls -A /hadoop/dfs/name)" ]; then
        echo "Namenode hasn't been formatted yet"
        $HADOOP_HOME/bin/hdfs namenode -format -force
    else
        echo "Namenode has been already formatted"
    fi
    $HADOOP_HOME/bin/hdfs --daemon start datanode
    $HADOOP_HOME/bin/yarn --daemon start nodemanager
    tail -f /dev/null

elif [ "$HADOOP_MODE" = "history" ]; then
    $SPARK_HOME/bin/spark-class org.apache.spark.deploy.history.HistoryServer

else
    echo "Undefined Mode $HADOOP_MODE, must specify: master, worker, history"

fi