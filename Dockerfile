FROM python:3.10
WORKDIR /is477
COPY requirements.txt requirements.txt
COPY scripts/* scripts/* 
RUN pip install -r requirements.txt