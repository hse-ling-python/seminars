# pull official base image
FROM python:3.8.3-slim-buster

# install system dependencies
RUN apt-get update  \
    && apt-get install -y netcat 

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
COPY /requirements/ /usr/src/app/requirements/
RUN pip3 install -r requirements/dev.txt

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]