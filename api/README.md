# Backend

Simple Flask API with CrewAI multiagents.


This project is using Python, Docker and CrewAI.

Check out CrewAI's [Getting started](https://github.com/joaomdmoura/crewAI?tab=readme-ov-file#getting-started) to get familiar with multi-agents.

## Installation

If you want to use Docker, check out the README.md in the root folder of this project.

### Linux

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

#### Run the API

```bash
python api.py
```
