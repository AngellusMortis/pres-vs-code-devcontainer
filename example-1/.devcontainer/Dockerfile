FROM python:3.10-slim-bullseye AS base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PATH /usr/local/bin/:$PATH

# create an app user to run code as
RUN groupadd -r python --gid 1000 && useradd --no-log-init -r --uid 1000 -m -g python python
RUN --mount=type=cache,mode=0755,target=/var/lib/apt/lists apt-get update && apt-get install -y git sudo \
    # upgrade pip
    && pip install --no-cache-dir -U pip

COPY ./requirements.txt /
RUN --mount=type=cache,mode=0755,target=/root/.cache/pip \
    pip install -r /requirements.txt \
    && rm /requirements.txt

# extra dev only env setup, like a prompt or letting app user run root
RUN echo 'export PS1="\[$(tput setaf 6)\]\w \[$(tput setaf 7)\]\\$ \[$(tput sgr0)\]"' >> /home/python/.bashrc \
    && echo 'python ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

USER python:python
