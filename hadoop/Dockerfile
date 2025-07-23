FROM python:3.10.18-slim-bullseye

# install base packages
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
                    build-essential \
                    software-properties-common \
                    libpq-dev \
                    openjdk-11-jdk \
                    wget
RUN rm -rf /var/lib/apt/lists/*

# download Hadoop
ENV HADOOP_VERSION=3.3.6
RUN wget -O apache-hadoop.tgz http://archive.apache.org/dist/hadoop/core/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
RUN mkdir -p /opt/hadoop
RUN tar -xf apache-hadoop.tgz -C /opt/hadoop --strip-components=1
RUN rm -rf apache-hadoop.tgz

# download spark
ENV SPARK_VERSION=3.4.1
ENV HADOOP_VERSION=3
RUN wget -O apache-spark.tgz https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
RUN mkdir -p /opt/spark
RUN tar -xf apache-spark.tgz -C /opt/spark --strip-components=1
RUN rm -rf apache-spark.tgz

# configure Hadoop
WORKDIR /opt/hadoop
ENV HADOOP_HOME=/opt/hadoop
ENV PATH=${HADOOP_HOME}/bin:${PATH}
ENV HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop
ENV HADOOP_OPTS=-Djava.library.path=/opt/hadoop/lib/native
ENV HDFS_NAMENODE_USER=root
ENV HDFS_DATANODE_USER=root
ENV YARN_RESOURCEMANAGER_USER=root
ENV YARN_NODEMANAGER_USER=root

# configure spark
WORKDIR /opt/spark
ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk-arm64"
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/sbin:/opt/spark/bin:${PATH}
ENV PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:${PATH}
ENV PATH=${PATH}:${JAVA_HOME}/bin
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3
ENV SPARK_MASTER_URL=spark://yarn-master:7077
ENV SPARK_MASTER_HOST=yarn-master
ENV SPARK_MASTER_PORT=7077
RUN mkdir /opt/spark/event
RUN chmod u+x /opt/spark/sbin/* && chmod u+x /opt/spark/bin/*

# install pyspark dependencies
COPY ./requirements.txt $SPARK_HOME/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r $SPARK_HOME/requirements.txt

# copy config file and start file from host
COPY ./spark-defaults.conf $SPARK_HOME/conf/spark-defaults.conf

# copy config files and start file from host
COPY ./config  $HADOOP_HOME/etc/hadoop/
COPY ./start-hadoop.sh $HADOOP_HOME/start-hadoop.sh

WORKDIR /opt
CMD ["/bin/bash", "/opt/hadoop/start-hadoop.sh"]