# Use 3.10 to allow nemo guardrails to work.
FROM mcr.microsoft.com/devcontainers/python:1-3.10-bullseye  

# Install AWS CLI for aarch64, refer to docs for more info https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
RUN apt-get update && \
    apt-get install -y curl unzip && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip" && \
    unzip -o awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip

# Install git and allow for git push/pull from devcontainer.
RUN apt-get install git && \
    git config --global --add safe.directory /workspaces/llm-experiments

# Install poetry via pip
ARG POETRY_VERSION=2.0.0
RUN pip3 install poetry==${POETRY_VERSION}
# Add the pypi index.
RUN poetry config repositories.pypi https://pypi.org/simple 


# Install pyenv

# Install python dependencies
# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt