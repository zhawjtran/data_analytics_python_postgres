FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04
LABEL maintainer=tranjoh

# Systemabhängigkeiten
RUN apt-get update && \
    apt-get -qy full-upgrade && \
    apt-get install -qy curl ca-certificates pkg-config libcairo2-dev libgirepository1.0-dev \
    gir1.2-gtk-3.0 build-essential libpq-dev gcc ninja-build && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Symlink setzen, damit `python` auf `python3` verweist
RUN ln -s /usr/local/python/current/bin/python3 /usr/bin/python

# Docker-Installation
RUN install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc && \
    chmod a+r /etc/apt/keyrings/docker.asc && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -qy docker-ce docker-ce-cli docker-compose-plugin && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Starship-Installation
RUN sh -c "$(curl -fsSL https://starship.rs/install.sh)" -- --yes && \
    mkdir -p /home/vscode/.config/ && \
    echo 'starship preset pure-preset -o /home/vscode/.config/starship.toml' >> /home/vscode/.bashrc && \
    echo 'eval "$(starship init bash)"' >> /home/vscode/.bashrc

# Standardnutzer des Dev Containers
USER vscode