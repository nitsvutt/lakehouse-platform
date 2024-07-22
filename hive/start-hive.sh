#!/bin/bash

if  [ "$HIVE_MODE" = "server" ];
then

$HIVE_HOME/bin/hiveserver2 --hiveconf hive.server2.enable.doAs=false

elif [ "$HIVE_MODE" = "metastore" ];
then

$HIVE_HOME/bin/schematool -initSchema -dbType $DATABASE_TYPE
$HIVE_HOME/bin/hive --service metastore

else

echo "Undefined Mode $HIVE_MODE, must specify: server, metastore"

fi