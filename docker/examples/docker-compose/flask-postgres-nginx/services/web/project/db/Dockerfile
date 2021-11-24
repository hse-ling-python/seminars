# pull official base image
FROM postgres:12-alpine

ARG POSTGRES_PASSWORD=postgres
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d