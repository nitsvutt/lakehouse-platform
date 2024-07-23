#!/bin/bash

$HIVE_METASTORE_HOME/bin/schematool -initSchema -dbType $DATABASE_TYPE
$HIVE_METASTORE_HOME/bin/start-metastore