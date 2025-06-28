# Base Image
FROM ubuntu:noble


# If the steps of a `Dockerfile` use files that are different from the `context` file, COPY the
# file of each step separately; and RUN the file immediately after COPY
WORKDIR /app
COPY /.devcontainer/requirements.txt /app


# Environment
SHELL [ "/bin/bash", "-c" ]


# Port
EXPOSE 8050


# ENTRYPOINT
ENTRYPOINT ["bash"]
