#!/bin/bash
set -e

echo logging in to ecr...CODEBUILD_WEBHOOK_TRIGGER
CODEBUILD_WEBHOOK_TRIGGER=branch/master

aws ecr get-login --no-include-email --region "$AWS_REGION"

if [[ "$CODEBUILD_WEBHOOK_TRIGGER" == "branch/master" ]] && [[ "$CODEBUILD_WEBHOOK_HEAD_REF" == "refs/heads/master" ]]
then
    DOCKER_TAG=prod
else
    DOCKER_TAG=${CODEBUILD_RESOLVED_SOURCE_VERSION}
fi

echo  Docker tag: "$DOCKER_TAG"

docker pull "$AWS_ACCOUNT_ID".dkr.ecr."$AWS_REGION".amazonaws.com/docker-flask:"$DOCKER_TAG" || true

export DOCKER_TAG=$DOCKER_TAG