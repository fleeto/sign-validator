#!/bin/sh
cp cosign-validation.py deploy/docker
docker build -t $1 deploy/docker