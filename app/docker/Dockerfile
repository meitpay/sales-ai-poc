FROM node:20-bookworm

WORKDIR /usr/src/app

# misc packages
RUN apt-get update && \
	apt-get install -y \
	zsh \
	git \
	vim \
	curl \
	wget \
	inetutils-tools \
    inetutils-ping \
	nano

USER node

# oh-my-zsh
RUN sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

# Run the application
CMD ["./docker/scripts/entrypoint.sh"]
