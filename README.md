# sequence-alignment-app

Submission of the backend coding challenge.

The objective of this exercise is to create a web application that can determine whether a particular DNA strand encodes a portion of a protein in a well-known set.

This web application serves a simple browser Javascript client (React) that takes a DNA sequence as input
and returns the name of the protein and where the sequence was found in the proteins sequence.

## Installation
This application depends on docker.

1) Install Docker
This code base is compatible with Docker v19.03.1 and Docker Compose v1.24.1

## Running the Application


To run the application in a development environment, just run 

```
docker-compose up --build
```
Then navigate to http://localhost:3000. 

This command will bring up the Flask app, celery worker, and redis.

## Shutting down the application
Press CTRL+C in your docker-compose terminal. Then:
```
docker-compose stop
```


## TODO
- Add tests to react app
- Documentation
- Cache results (no need to search for duplicate sequence)
