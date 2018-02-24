#!/usr/bin/env bash

docker build -t task1_viewer ./viewer
docker run -i --network=task1_default task1_viewer
