ARG SPARK_VERSION=3.4.1
FROM nitsvutt/spark:$SPARK_VERSION

# download Hadoop
ENV HADOOP_VERSION=3.3.6
RUN wget -O apache-hadoop.tgz http://archive.apache.org/dist/hadoop/core/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
RUN mkdir -p /opt/hadoop
RUN tar -xf apache-hadoop.tgz -C /opt/hadoop --strip-components=1
RUN rm -rf apache-hadoop.tgz

# configure Hadoop
WORKDIR /opt/hadoop
ENV HADOOP_HOME=/opt/hadoop
ENV PATH=${HADOOP_HOME}/bin:${PATH}
ENV HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop
ENV HADOOP_OPTS=-Djava.library.path=/opt/hadoop/lib/native
ENV YARN_RESOURCEMANAGER_USER=root
ENV YARN_NODEMANAGER_USER=root

# copy config files from host
COPY ./config $HADOOP_HOME/etc/hadoop/

# init directories and files
RUN mkdir -p /project
COPY ./requirements.txt /project/requirements.txt

# install packages
WORKDIR /project
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt