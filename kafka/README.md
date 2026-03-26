# Set up Iceberg Sink Connector
- Clone git project:
```
git clone https://github.com/databricks/iceberg-kafka-connect.git
```

- Build project (using Java 17+ and Gradle 8+):
```
cd iceberg-kafka-connect
```
```
./gradlew -xtest clean build
```

- Unzip package:
```
unzip ./kafka-connect-runtime/build/distributions/iceberg-kafka-connect-runtime-hive-0.7.0-dev.1+4ac3ebb.zip -d ../lakehouse-platform/kafka/iceberg-kafka-connect-runtime-hive
```