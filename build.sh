#!/usr/bin/env bash

docker build api -t infra-gunicorn-api

docker build front -t infra-gunicorn-front


