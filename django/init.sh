#!/bin/bash
python3 tashis/manage.py migrate

DJANGO_SUPERUSER_PASSWORD=admin python3 tashis/manage.py createsuperuser --no-input --username=admin --email=admin@mail.com

python3 tashis/manage.py makemigrations

python3 tashis/manage.py migrate
