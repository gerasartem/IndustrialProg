#!/usr/bin/env bash

docker build -t task1_producer ./producer
docker run -i --network=task1_default task1_producer
