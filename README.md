# ginkgo-backend-challenge

Submission of the Ginkgo backend coding challenge.

This web application serves a simple browser Javascript client (React) that takes a DNA sequence as input
and returns the name of the protein and where the sequence was found in the proteins sequence.

## Installation
This application depends on docker.

1) Install Docker
This code base is compatible with Docker v19.03.1 and Docker Compose v1.24.1

## Running the Application


To run the application in a development environment, just run 

```
docker-compose up -d --build
```
Then navigate to http://localhost:3000. 

This command will bring up the Flask app, celery worker, and redis. 
