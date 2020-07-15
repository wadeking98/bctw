FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update

RUN pip install -r requirements.txt

RUN apt-get install -y binutils libproj-dev gdal-bin libgdal-dev python3-gdal

RUN pip install psycopg2-binary

RUN pip install django djangorestframework

COPY . /code/
WORKDIR /code


EXPOSE 8000
CMD ["python3", "tashis/manage.py", "runserver", "0.0.0.0:8000"]