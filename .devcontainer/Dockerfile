FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04
LABEL maintainer=tranjoh

# System Dependencies install and update
RUN apt-get update && \
    apt-get -qy full-upgrade && \
    apt-get install -qy python3 python3-pip python3-venv curl ca-certificates && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install docker engine, docker cli and also docker plugins
# I follow this document: https://docs.docker.com/engine/install/ubuntu/
RUN \
    apt-get update && \
    install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc && \
    chmod a+r /etc/apt/keyrings/docker.asc

# Install kernel
RUN pip install ipykernel jupyter

RUN echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN \
    apt-get update && \
    apt-get install -qy \
    docker-ce docker-ce-cli docker-compose-plugin

# Install starship for vscode user with pure prompt
RUN \
    sh -c "$(curl -fsSL https://starship.rs/install.sh)" -- --yes && \
    mkdir -p /home/vscode/.config/ && \
    echo 'starship preset pure-preset -o /home/vscode/.config/starship.toml'  >> /home/vscode/.bashrc && \
    echo 'eval "$(starship init bash)"' >> /home/vscode/.bashrc

# default user of dev container
USER vscode
