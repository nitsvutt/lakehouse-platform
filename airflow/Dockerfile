FROM apache/airflow:2.8.2

# install base packages
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         openjdk-17-jre-headless \
         wget \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# install apache spark provider
USER airflow
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" apache-airflow-providers-apache-spark

USER root
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
# configure hadoop
ENV HADOOP_HOME=/opt/hadoop
ENV PATH=${HADOOP_HOME}/bin:${PATH}
ENV HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop
ENV HADOOP_OPTS=-Djava.library.path=/opt/hadoop/lib/native
ENV HDFS_NAMENODE_USER=root
ENV HDFS_DATANODE_USER=root
ENV YARN_RESOURCEMANAGER_USER=root
ENV YARN_NODEMANAGER_USER=root
# configure spark
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/sbin:/opt/spark/bin:${PATH}
ENV PATH=$HADOOP_HOME/bin:$HADOOP_HOME/sbin:${PATH}
ENV PATH=${PATH}:${JAVA_HOME}/bin
ENV PYSPARK_PYTHON=/usr/bin/python
ENV PYSPARK_DRIVER_PYTHON=/usr/bin/python
ENV SPARK_MASTER_URL=spark://yarn-master:7077
ENV SPARK_MASTER_HOST=yarn-master
ENV SPARK_MASTER_PORT=7077
RUN mkdir /opt/spark/event
RUN chmod u+x /opt/spark/sbin/* && chmod u+x /opt/spark/bin/*

# update python to run mode client
RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3.8 1