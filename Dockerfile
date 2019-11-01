FROM node:13.0.1-alpine AS buildstep
LABEL maintainer "Bob Fratantonio <bob.frat@gmail.com>"

RUN mkdir -p /app
WORKDIR /app

COPY ./app/ui/package.json /app/package.json
COPY ./app/ui/package-lock.json /app/package-lock.json

RUN npm install

COPY ./app/ui /app
RUN npm run build

FROM python:3.6

RUN apt-get update

RUN mkdir /app
WORKDIR /app
COPY . /app
COPY --from=buildstep /app/build /app/app/ui

RUN pip install --no-cache-dir -r requirements-dev.txt

ENV FLASK_ENV="development"

EXPOSE 3000
