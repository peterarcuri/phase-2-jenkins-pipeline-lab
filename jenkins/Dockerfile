FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
    docker.io \
    curl \
    wget \
    gnupg \
    lsb-release && \
    rm -rf /var/lib/apt/lists/*

USER jenkins