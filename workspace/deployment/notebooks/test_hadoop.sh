#!/bin/bash

$HADOOP_HOME/bin/hdfs dfs -mkdir hdfs://namenode:9000/user/hive/spark_jars

$HADOOP_HOME/bin/hdfs dfs -put /project/deployment/spark_jars/*.jar hdfs://namenode:9000/user/hive/spark_jars

$HADOOP_HOME/bin/hdfs dfs -ls hdfs://namenode:9000/user/hive/spark_jars