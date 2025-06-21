ARG JDK_VERSION=11.0.16-jre-slim-buster
ARG PYTHON_VERSION=3.10.4

FROM openjdk:$JDK_VERSION

# install base packages
RUN apt-get update
RUN apt-get install build-essential \
                    zlib1g-dev \
                    libncurses5-dev \
                    libgdbm-dev \
                    libnss3-dev \
                    libssl-dev \
                    libreadline-dev \
                    libffi-dev \
                    libsqlite3-dev \
                    wget \
                    libbz2-dev \
                    procps \
                    software-properties-common \
                    libpq-dev \
                    ca-certificates -y
RUN rm -rf /var/lib/apt/lists/*

# download python
ARG PYTHON_VERSION
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz
RUN mkdir -p /opt/python
RUN tar -xf Python-${PYTHON_VERSION}.tgz -C /opt/python --strip-components=1
RUN rm -rf Python-${PYTHON_VERSION}.tgz

# intsall python
WORKDIR /opt/python
RUN ./configure --enable-optimizations
RUN make -j $(nproc)
RUN make altinstall
RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3.10 1

# download and install pip
RUN curl https://bootstrap.pypa.io/get-pip.py | python
RUN update-alternatives --install /usr/bin/pip pip /usr/local/bin/pip3.10 1

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