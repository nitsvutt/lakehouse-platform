ARG JDK_VERSION=11.0.16-jre-slim-buster

FROM openjdk:$JDK_VERSION

# install base packages
RUN apt-get update
RUN apt-get install build-essential \
                    wget -y
RUN rm -rf /var/lib/apt/lists/*

# download Hadoop
ENV HADOOP_VERSION=3.3.6
RUN wget -O apache-hadoop.tgz http://archive.apache.org/dist/hadoop/core/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
RUN mkdir -p /opt/hadoop
RUN tar -xf apache-hadoop.tgz -C /opt/hadoop --strip-components=1
RUN rm -rf apache-hadoop.tgz

# download Hive
ENV HIVE_VERSION=4.0.0
RUN wget -O apache-hive.tgz https://downloads.apache.org/hive/hive-$HIVE_VERSION/apache-hive-$HIVE_VERSION-bin.tar.gz
RUN mkdir -p /opt/hive
RUN tar -xf apache-hive.tgz -C /opt/hive --strip-components=1
RUN rm -rf apache-hive.tgz

# download PostgreSQL connector
ENV POSTGRES_CONNECTOR_VERSION=42.7.3
RUN wget -O /opt/postgresql-$POSTGRES_CONNECTOR_VERSION.jar https://jdbc.postgresql.org/download/postgresql-$POSTGRES_CONNECTOR_VERSION.jar
RUN ln -s /opt/postgresql-$POSTGRES_CONNECTOR_VERSION.jar /opt/hadoop/share/hadoop/common/lib/
RUN ln -s /opt/postgresql-$POSTGRES_CONNECTOR_VERSION.jar /opt/hive/lib/

# configure Hadoop
ENV HADOOP_HOME=/opt/hadoop
ENV PATH=${HADOOP_HOME}/bin:${PATH}

# configure Hive
ENV HIVE_HOME=/opt/hive
ENV PATH=${HIVE_HOME}/bin:${PATH}

# configure PosgreSQL connector
ENV DATABASE_DRIVER=org.postgresql.Driver
ENV DATABASE_TYPE=postgres
ENV DATABASE_TYPE_JDBC=postgresql
ENV DATABASE_HOST=postgresql
ENV DATABASE_PORT=5432

# copy config file and start file from host
COPY ./config/hive-site.xml  $HIVE_HOME/conf/hive-site.xml
COPY start-hive.sh $HIVE_HOME

CMD ["/bin/bash", "/opt/hive/start-hive.sh"]
