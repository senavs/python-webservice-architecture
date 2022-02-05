# Python Webservice Architecture

Base Python3 webservice architecture for future projects.

## Objective

The main objective of this architecture is split all components into 5 parts and remove
correlation between them.

Be side that, detach the entrypoint layer from the others so that we can easily change
framework or communication protocol. Eg: change FastAPI to Flask or HTTP to GRPC.

See [components](#components) session for more information.

## Requirements (Programs & Libs)

To run the project, you can only have `docker` and `docker-compose`.
The `docker-compose.yml` file contains the database and application image.

If you prefer to run without containers, you need to have installed Python3.10, Postgres
Database and all required libraries (`requirements.txt`).

## Run it

After clone this project, you can flow the next instructions to run it.

### With Docker

This command will build application image and set up a container based on this image and
other with Postgres database.

```shell
docker-compose up
```

### Without Docker

To run without container, you have to have
installed [Python3.10](https://www.python.org/)
and [Postgres](https://www.postgresql.org/download/) first.

After installed them, run the following command to install all Python required libraries.

```shell
pip install -r ./api/requirements.txt
```

OR

```shell
pip3 install -r ./api/requirements.txt
```

**NOTE:** Remember to configure the local Postgres database settings in `api/settings.py`
, if needed.

### Test it

For both strategy (with/without Docker), open your browser in http://localhost:8080/docs.
If a swagger page is opened, it's done!

## Components

![architecture diagram](_images/architecture/diagram.png)

## How to add new features
