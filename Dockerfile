FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /enactus
WORKDIR /enactus

RUN pip install -r requirments/requirments-dev.txt
