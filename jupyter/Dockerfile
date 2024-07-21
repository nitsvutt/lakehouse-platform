ARG SPARK_VERSION=3.4.1
FROM nitsvutt/spark:$SPARK_VERSION

# init directories and files
RUN mkdir -p /project
COPY requirements.txt /project/requirements.txt

# install packages
WORKDIR /project
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt