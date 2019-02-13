FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

RUN cat /etc/os-release
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install mysql-client
COPY . /code/

COPY ./docker/entrypoint.sh /code/

RUN chmod 755 entrypoint.sh
