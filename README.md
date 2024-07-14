# Microservices Template

## About Project
Tiny microservice template with docker and other local configuration

### App contains:
* app
* tests


## Tech Stack
* Python
* FastAPI
* PostgreSQL
* Docker
* Docker-compose


### Linux 

First you need to clone`git@github.com:DiddyChriss/mst.git`

Follow the instructions below:

1. include provided by author variables into `.example.env`
2. run `make first_setup`
3. each subsequent run `make setup`

A specific Super User is created during the setup, with the following credentials provided in the `.env` file:

File `Makefile` contains all the commands needed to run the project.

### Documentation
* Available on `/docs/` path.

### Troubleshooting
* Make sure all dependencies are properly installed.
* Docker and Postgres are the proper version installed.
* In case of any problems with the installation, please report to the author of the project.
