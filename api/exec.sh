#!/bin/bash

# Stop and remove containers, networks
docker compose down

# Create and start containers see docker compose up --help
docker compose up "$@" --build
