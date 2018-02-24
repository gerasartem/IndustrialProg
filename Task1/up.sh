#!/usr/bin/env bash

docker-compose build
docker-compose up -d task_db rabbitmq
sleep 10
docker-compose up consumer
