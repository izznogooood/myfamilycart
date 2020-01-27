FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk update --no-cache \
    && apk add --no-cache --virtual build-deps gcc python3-dev musl-dev postgresql-dev bash 

RUN pip install --upgrade pip
COPY ./requirements.txt /app/.
RUN pip install -r requirements.txt
RUN apk del build-deps

COPY . /app 

