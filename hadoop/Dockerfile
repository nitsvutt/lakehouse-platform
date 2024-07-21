ARG JDK_VERSION=11.0.16-jre-slim-buster

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
                    ca-certificates -y
RUN rm -rf /var/lib/apt/lists/*

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

# HDFS: NameNode (NN):
#	9000 = fs.defaultFS
#	9870 = dfs.http.address
# HDFS: DataNode (DN):
#	9866 = dfs.datanode.address
#	9867 = dfs.datanode.ipc.address
#	9865 = dfs.datanode.http.address
# YARN: Resource Manager:
#   8031 = yarn.resourcemanager.resource-tracker.address
#   8088 = yarn.resourcemanager.webapp.address
#   8042 = yarn.nodemanager.webapp.address
#   8188 = yarn.timeline-service.webapp.address
EXPOSE 9000 9870 9866 9867 9865 8031 8088 8042 8188

# copy config files and start file from host
COPY ./config  $HADOOP_HOME/etc/hadoop/
COPY start-hadoop.sh $HADOOP_HOME

CMD ["/bin/bash", "$HADOOP_HOME/start-hadoop.sh"]