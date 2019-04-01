#!/bin/bash

echo "Waiting for postgres..."

while ! nc -z $SQL_HOST $SQL_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py makemigrations --settings=myfamily.settings.pro
python manage.py migrate --settings=myfamily.settings.pro
python manage.py collectstatic --no-input --settings=myfamily.settings.pro

gunicorn myfamily.wsgi:application --bind 0.0.0.0:8000
