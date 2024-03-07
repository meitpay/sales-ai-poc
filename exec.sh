#!/bin/bash

# Stop and remove containers, networks
docker compose down

# Check if the first argument is --no-cache
if [ "$1" = "--no-cache" ]; then
    echo "Detected --no-cache argument. Running 'docker compose build' without cache."

    # Run docker compose build with no cache
    docker compose build --no-cache

    # Remove the first argument (--no-cache) from the arguments list
    shift

    # Create and start containers without the --build option
    docker compose up "$@"
else
    # Create and start containers with the --build option
    docker compose up "$@" --build
fi
