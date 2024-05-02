# Backend

Simple Flask API with CrewAI multi-agents.

This project is using Python, Docker and CrewAI.

Check out CrewAI's [Getting started](https://github.com/joaomdmoura/crewAI?tab=readme-ov-file#getting-started) to get familiar with multi-agents.

## Installation

If you want to use Docker, check out the README.md in the root folder of this project.

### Linux

#### Make sure you have python installed

```bash
sudo apt install python3 python3-pip ipython3 python3-venv
```

#### Add python to ``$PATH`` and add an alias in your bash environment

```bash
PATH=”$PATH:/usr/bin/python3”
alias python=python3
```

#### Create a python virtual environment

```bash
python -m venv venv
```

#### Activate the virtual environment

```bash
source venv/bin/activate
```

#### Install dependencies

```bash
pip install --no-cache-dir -r requirements.txt
```

#### Env variables

Copy `.env.example` to `.env` and populate it

```bash
cp .env.example .env
```

````dotenv
# Required
OPENAI_API_KEY=""
SERPER_API_KEY=""

# Required for social media search
PROXY_CURL_TOKEN=""
PROXY_CURL_MOCK_DATA=True

# Optional - change these variables if you like
OPENAI_MODEL_NAME="gpt-3.5-turbo"
APP_ENV="development"
APP_PORT=5000
````

#### Proxy Curl

[ProxyCurl](https://nubela.co/proxycurl/docs?shell#people-api-person-profile-endpoint) 
is used to get person data from LinkedIn, Twitter and Facebook.
To call the API directly, make sure to populate the ``PROXY_CURL_TOKEN`` variable, and set ``PROXY_CURL_MOCK_DATA`` to ``False``.

During development, you can use the [generateSoMeExamples.sh](io/templates/generateSoMeExamples.sh) to call the API once and use save the response for to avoid calling the API every time.

Make sure to populate the ``PROXY_CURL_TOKEN`` variable, and set ``PROXY_CURL_MOCK_DATA`` to ``True`` and populate the public identifiers in the [script](io/templates/generateSoMeExamples.sh).

````bash
LINKED_IN_PUBLIC_IDENTIFIER="<public identifier>"
TWITTER_PUBLIC_IDENTIFIER="<public identifier>"
FACEBOOK_PUBLIC_IDENTIFIER="<public identifier>"
````



#### Run the API

```bash
python app.py
```
