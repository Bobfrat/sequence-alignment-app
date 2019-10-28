FROM python:3.6

LABEL maintainer "Bob Fratantonio <bob.frat@gmail.com>"

RUN apt-get update

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements-dev.txt

ENV FLASK_ENV="development"

EXPOSE 3000