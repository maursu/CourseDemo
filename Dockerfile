FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /eduspace
WORKDIR /eduspace

RUN pip install -r requirments/requirments-dev.txt
