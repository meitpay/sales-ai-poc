# Sales AI

PoC

## Getting Started

This project is using Python, Docker and CrewAI.

Check out CrewAI's [Getting started](https://github.com/joaomdmoura/crewAI?tab=readme-ov-file#getting-started) to get familiar with multi-agents.

### Linux

You can either setup the application on your computer or use Docker.

#### Installation

**Make sure you have python installed**

```bash
sudo apt install python3 python3-pip ipython3 python3-venv
```

**Add python to ``$PATH`` and add an alias in your bash environment**

```bash
PATH=”$PATH:/usr/bin/python3”
alias python=python3
```

**Create a python virtual environment**

```bash
python -m venv venv
```

**Activate the virtual environment**

```bash
source venv/bin/activate
```

**Install dependencies:**

```bash
pip install --no-cache-dir -r requirements.txt
```

**Env variables**

Copy `.env.example` to `.env` and populate it

```bash
cp .env.example .env
```


### Docker

Make sure you have [Docker](https://docs.docker.com/get-docker/) installed.

Copy `.env.example` to `.env` and populate with your OpenAI API key

```bash
cp .env.example .env
```

## Run the Application

### Linux

Run `python api.py` to start the API.

### Docker

**Linux/WSL/Mac**

- Run the `exec.sh` script with optional params; run `docker compose up --help` for options
- Run `docker compose exec api zsh` to enter the shell of the application in Docker

**Windows**

- Run `docker compose down` to stop and remove containers and networks
- Run `docker compose up -d --build` to create and start the application in detached mode
