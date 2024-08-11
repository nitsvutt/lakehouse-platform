ARG UBUNTU_VERSION=22.04
ARG PYTHON_VERSION=3.10.4

FROM ubuntu:$UBUNTU_VERSION

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

# init directories and files
RUN mkdir -p /app
COPY ./requirements.txt /app/requirements.txt

# install packages
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt