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
    postgresql-client \
    curl ca-certificates && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Erstelle ein Verzeichnis für dein Projekt und setze es als Arbeitsverzeichnis
WORKDIR /workspace

# Optional: Python-Abhängigkeiten direkt hier installieren
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Aktiviere den Python-Shell-Zugriff und ggf. andere Umgebungsvariablen
ENV PYTHONUNBUFFERED=1

# Setze den Standardbenutzer, falls nötig
USER vscode

# Stelle sicher, dass der Docker-Dienst (dank dind) im Container läuft, wenn er in Codespaces verwendet wird
