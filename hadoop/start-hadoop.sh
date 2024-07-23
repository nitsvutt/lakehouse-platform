#!/bin/bash

if [ "$HADOOP_MODE" = "namenode" ]; then
    $HADOOP_HOME/bin/hdfs --config $HADOOP_CONF_DIR namenode --no-prompt -format
    $HADOOP_HOME/bin/hdfs --config $HADOOP_CONF_DIR namenode

elif [ "$HADOOP_MODE" = "datanode" ]; then
    $HADOOP_HOME/bin/hdfs --config $HADOOP_CONF_DIR datanode

elif [ "$HADOOP_MODE" = "resourcemanager" ]; then
    $HADOOP_HOME/bin/yarn --config $HADOOP_CONF_DIR resourcemanager

elif [ "$HADOOP_MODE" = "nodemanager" ]; then
    $HADOOP_HOME/bin/yarn --config $HADOOP_CONF_DIR nodemanager

elif [ "$HADOOP_MODE" = "timelineserver" ]; then
    $HADOOP_HOME/bin/yarn --config $HADOOP_CONF_DIR timelineserver

elif [ "$HADOOP_MODE" = "client" ]; then
    echo "HADOOP CLIENT"

else
    echo "Undefined Mode $HADOOP_MODE, must specify: namenode, datanode, resourcemanager, nodemanager, timelineserver, client"

fi