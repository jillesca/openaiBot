# syntax=docker/dockerfile:1
FROM python:3.11.2 AS base 
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

FROM base AS arg
WORKDIR /home

ARG OPENAI_KEY
ENV OPENAI_KEY $OPENAI_KEY
ARG OPENAI_ORG
ENV OPENAI_ORG $OPENAI_ORG

FROM arg AS prod
COPY ./openai .

FROM arg AS dev
ARG DEV 
ENV DEV $DEV


# build base image from ROOT dir
# source .env 
# docker build --build-arg OPENAI_KEY=$OPENAI_KEY --build-arg OPENAI_ORG=$OPENAI_ORG --target dev --file openai.dockerfile --tag jillesca/python:openai0.1 .
# docker run -d -it --name openai --mount type=bind,source="$(pwd)/openai",target=/home/openai jillesca/python:openai0.1
# 
# docker exec -it openai /bin/bash