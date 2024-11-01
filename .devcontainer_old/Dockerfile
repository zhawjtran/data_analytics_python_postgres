#FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.10
#
#RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#    && apt-get -y install --no-install-recommends postgresql-client \
#    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04
LABEL maintainer="tranjoh@students.zhaw.ch"

# Systemabhängigkeiten installieren
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv \
    curl ca-certificates && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install docker engine, docker cli and also docker plugins
# I follow this document: https://docs.docker.com/engine/install/ubuntu/
RUN \
    apt-get update && \
    install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc && \
    chmod a+r /etc/apt/keyrings/docker.asc

RUN echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN \
    apt-get update && \
    apt-get install -qy \
    docker-ce docker-ce-cli docker-compose-plugin

# Erstelle ein Verzeichnis für dein Projekt und setze es als Arbeitsverzeichnis
WORKDIR /workspace

# Optional: Python-Abhängigkeiten direkt hier installieren
#COPY requirements.txt .
#RUN pip3 install --no-cache-dir -r requirements.txt

# Aktiviere den Python-Shell-Zugriff und ggf. andere Umgebungsvariablen
ENV PYTHONUNBUFFERED=1

# Setze den Standardbenutzer, falls nötig
USER vscode

# Stelle sicher, dass der Docker-Dienst (dank dind) im Container läuft, wenn er in Codespaces verwendet wird
