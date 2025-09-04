FROM cnfldemos/cp-server-connect-datagen:0.6.4-7.6.0

RUN /bin/confluent-hub install --no-prompt debezium/debezium-connector-mysql:2.4.2
RUN /bin/confluent-hub install --no-prompt debezium/debezium-connector-postgresql:2.5.4
RUN /bin/confluent-hub install --no-prompt confluentinc/kafka-connect-hdfs3:1.2.0