# Pull a base image
FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN \
  apt-get update \
  && apt-get install -y \
      apt-utils \
      gcc wget telnet \
      curl make \
      build-essential \
      cmake \
      git \
      pkg-config \
      iputils-ping \
      net-tools  \
      libcurl4-openssl-dev libssl-dev gcc\
    && rm -rf /var/lib/apt/lists/*

RUN useradd seedlist

COPY scripts .
COPY server/wsgi/gunicorn_config.py .

RUN pip install --upgrade pip

COPY ./dist/deps/*.whl ./
RUN pip install *.whl && rm -rf *.whl

COPY ./dist/*.whl ./
RUN pip install *.whl && rm -rf *.whl

RUN sed -i '/CipherString = DEFAULT/s/^#\?/#/' /etc/ssl/openssl.cnf

# EXPOSE 8000

USER seedlist
