FROM postgres:12

WORKDIR /

ADD dbscripts /docker-entrypoint-initdb.d

RUN apt-get update

RUN apt-get -y install jq

RUN apt-get -y install postgis

EXPOSE 5432
