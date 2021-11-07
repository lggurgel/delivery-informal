FROM python:3.8-slim-buster

WORKDIR /backend

# prevent python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# prevent python from buffering stdout and stderr
ENV PYTHONBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql libpq-dev \
    && apt-get clean

RUN pip install --upgrade pip

COPY ./requirements.txt /backend/requirements.txt

RUN pip install -r requirements.txt

COPY . /backend/
