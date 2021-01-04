FROM alpine:latest

WORKDIR /code

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/code
RUN apk update
RUN apk add bash
RUN apk add curl
RUN apk add gcc
RUN apk add g++
RUN apk add libffi-dev build-base openssl-dev
RUN apk add --update --no-cache python3 && ln -sf pyhton3 /usr/bin/python
RUN apk add python3-dev
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

COPY pyproject.toml .
COPY poetry.lock .
RUN pip3 install poetry

COPY backend/ ./backend
COPY start.sh .

RUN poetry install

CMD [ "./start.sh" ]