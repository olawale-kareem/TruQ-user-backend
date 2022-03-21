# [TruQ user API](https://github.com/olawale-kareem/TruQ-backend)

TruQ User API Service

## Technologies

- [Python 3.9](https://python.org) : Base programming language for development
- [PostgreSQL](https://www.postgresql.org/) : Application relational databases for development, staging and production environments
- [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
- [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
- [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration

## Description

## Getting Started

```docker

1. clone project repository:   git clone git@github.com:olawale-kareem/TruQ-user-backend.git
2. change to project folder:   cd TruQ-user-backend
3. build the image:            docker-compose build
4. start container services:   docker-compose up

```

## Access running services/containers

App services in active containers can be accessed via the commands below. Once in the respective containers django and postgres commands can be used.

```services

web: docker exec -it truq_backend bash
db : docker exec -it postgresDB  psql -U postgres

```

## Running Tests

Before running the tests with the following command make sure that the web service is up and running. Run the following command below

```web service

docker exec -it truq_backend bash;
python manage.py test

```

## Author

[![](https://github.com/olawale-kareem.png)](https://github.com/olawale-kareem)
