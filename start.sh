#!/bin/bash

python manage.py migrate
gunicorn config.wsgi:application -w 2 -b :${APP_PORT}