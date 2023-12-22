#!/bin/bash


if [[ $1 = 'config' ]]; then

    cat .env.example >> kernel/.env
    echo ".env создан"
    echo "Обязательно смените SECRET_KEY"
    echo "Так же не забудьте настроить SMTP и SMS"
fi

if [[ $1 = 'deploy' ]]; then
	
    docker-compose up -d --build kernel

fi
