#!/bin/bash



if [[ $1 = 'app' ]]; then
    ./dmanage.py startapp --template app_template $2
    exit 0
fi

if [[ $1 = 'run' ]]; then
    ./dmanage.py runserver 0.0.0.0:8000
    exit 0
fi

if [[ $1 = 'migrate' ]]; then
    ./dmanage.py makemigrations
    ./dmanage.py migrate
    exit 0
fi


if [[ $1 = 'pip' ]]; then
    pip install -r requirements.txt
    cat requirements.txt > .devcontainer/requirements.txt
    exit 0
fi

if [[ $1 = 'su' ]]; then
    ./dmanage.py createsuperuser
    exit 0
fi

./dmanage.py $@
