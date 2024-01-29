FROM python:3.11


RUN apt-get update -y \
    && apt-get upgrade -y

RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3.11 1

RUN python3 -m pip install --upgrade pip

COPY requirements.txt requirements.txt

WORKDIR /src/
RUN alias python3='python3.11'
RUN python3 -m pip install --upgrade pip setuptools
RUN pip3 install -r ../requirements.txt
RUN pip install jupyterlab
