#!/bin/bash


if [[ $1 = 'config' ]]; then

    cat .env.example >> kernel/.env
    echo ".env создан"
fi

if [[ $1 = 'deploy' ]]; then
    
    docker-compose up -d --build 

fi
