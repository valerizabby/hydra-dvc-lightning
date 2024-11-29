FROM ubuntu:22.04

RUN apt update
RUN apt-get install -y g++ python3 libopenblas-dev pip vim git tree
RUN apt-get install -y libgtest-dev
RUN apt-get install -y python3.10-venv
RUN apt-get install -y tree make

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/valerizabby/MeanVector.git

WORKDIR /MeanVector