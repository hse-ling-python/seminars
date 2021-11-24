#!/bin/bash
set -e

TAG_NAME="$AWS_ACCOUNT_ID".dkr.ecr."$AWS_REGION".amazonaws.com/docker-flask:$DOCKER_TAG

echo building and testing dev images...

docker-compose up -d --build
docker-compose exec -T web python -m pytest "project/tests" -p no:warnings --cov="project"
docker-compose exec -T web flake8 --ignore=E501,F401 project
docker-compose exec -T web black project --check
docker-compose exec -T web /bin/sh -c "isort project/*/*.py --check-only"

echo building prod images...

docker build \
    -t "$TAG_NAME" \
    -f services/web/Dockerfile.prod \
    ./services/web