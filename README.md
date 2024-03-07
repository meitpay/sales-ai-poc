# Multi Agent Sales AI

This Project is setup using two Docker containers; `api` and `app`.

If you do not wish to use docker check out [API README.md](api/README.md) and [APP README.md](app/README.md) to setup the environment needed to run these applications.

## Getting started

Make sure you have [Docker](https://docs.docker.com/get-docker/) installed.

### Docker

Copy `.env.example` to `.env` and populate it.

```bash
cp ./api/.env.example ./api/.env
cp ./app/.env.example ./app/.env
```

## Run the Application

General Docker compose docs; `docker compose --help`

**Linux/Mac**

Run the `exec.sh` script with optional params.
 - If the first param is `--no-cache` a build without cache will be used
 - Run `docker compose up --help` for other params

**Windows and other alternatives**

- Run `docker compose down` to stop and remove containers and networks
- Run `docker compose build --no-cache` if you do not want to use cache when building the image
- Run `docker compose up -d --build` to build, create and start the application in detached mode

**execute commands inside the running container**

Run `docker compose exec [OPTIONS] SERVICE COMMAND [ARGS...]` to execute commands in the container
- e.g. `docker compose exec app zsh` to enter the shell of the container.
