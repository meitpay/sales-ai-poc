FROM python:3.12.2-bookworm

WORKDIR /usr/src/api

# misc packages
RUN apt-get update && \
	apt-get install -y \
	zsh \
	git \
	vim \
	curl \
	nano

# oh-my-zsh
RUN sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

# Install any needed packages specified in requirements.txt
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Keep the container alive, currently we're only running a simple script
CMD ["python", "api.py"]
