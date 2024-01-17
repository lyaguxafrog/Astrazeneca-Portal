#!/bin/bash

./manage.sh migrate --no-input
./manage.sh collectstatic --no-input

gunicorn -c  config/guvicorn.config.py config.wsgi:application --enable-stdio-inheritance
