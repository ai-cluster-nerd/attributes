# Base Image
FROM ubuntu:noble-20250529


# If the steps of a `Dockerfile` use files that are different from the `context` file, COPY the
# file of each step separately; and RUN the file immediately after COPY
WORKDIR /app
COPY /.devcontainer/requirements.txt /app


# Environment
SHELL [ "/bin/bash", "-c" ]


# Setting Up
ENV TZ=Europe/London
RUN apt clean && apt -q -y update && apt -q -y upgrade && apt -y install sudo && \ 
    apt install -y tzdata && ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && apt clean && \
    apt -y install graphviz vim unzip wget curl && \
    apt -y install software-properties-common && \ 
    add-apt-repository ppa:git-core/ppa && apt -y install git-all && \
    apt install -y build-essential libssl-dev libffi-dev && \
    apt install -y python3 python3-dev python3-pip python3-yaml python3-venv


# Port
EXPOSE 8050


# ENTRYPOINT
ENTRYPOINT ["bash"]
