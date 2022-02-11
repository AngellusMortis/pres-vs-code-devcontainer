FROM python:3.10-slim-bullseye AS base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH /code/
ENV PATH /usr/local/bin/:$PATH

# create an app user to run code as
RUN groupadd -r python --gid 1000 && useradd --no-log-init -r --uid 1000 -m -g python python
RUN --mount=type=cache,mode=0755,target=/var/lib/apt/lists apt-get update && apt-get install -y git \
    # upgrade pip
    && pip install --no-cache-dir -U pip \
    # setup app user and working directory
    && mkdir -p /code/


## intermediate image to build deps
FROM base as builder
# build time only deps
RUN --mount=type=cache,mode=0755,target=/var/lib/apt/lists apt-get update && apt-get install -y build-essential
COPY ./requirements.txt /
RUN --mount=type=cache,mode=0755,target=/root/.cache/pip \
    pip install -r /requirements.txt \
    && rm /requirements.txt


## intermediate dev image to build deps
FROM builder as builder-dev
COPY ./dev-requirements.txt /dev-requirements.txt
RUN --mount=type=cache,mode=0755,target=/root/.cache/pip \
    pip install -r /dev-requirements.txt \
    && rm /dev-requirements.txt


## development only build
FROM base as dev
COPY --from=builder-dev /usr/local/bin/ /usr/local/bin/
COPY --from=builder-dev /usr/local/lib/python3.10/ /usr/local/lib/python3.10/

# dev only deps you do not want in your "prod" image
RUN --mount=type=cache,mode=0755,target=/var/lib/apt/lists apt-get update && apt-get install -y sudo vim curl procps jq
# extra dev only env setup, like a prompt or letting app user run root
RUN echo 'export PS1="\[$(tput setaf 6)\]\w \[$(tput setaf 7)\]\\$ \[$(tput sgr0)\]"' >> /home/python/.bashrc \
    && echo 'python ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

USER python:python
WORKDIR /code/
EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]


## production only build
FROM base as prod
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /usr/local/lib/python3.10/ /usr/local/lib/python3.10/

USER python:python
WORKDIR /code/
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
