FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update

RUN pip install -r requirements.txt

RUN apt-get install -y binutils libproj-dev gdal-bin libgdal-dev python3-gdal

COPY . /code/
WORKDIR /code


EXPOSE 8000
CMD ["/bin/bash", "-c", "init.sh"]