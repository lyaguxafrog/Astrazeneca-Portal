#!/bin/bash


if [[ $1 = 'config' ]]; then

    cat .env.example >> kernel/.env
    echo ".env создан"
fi

if [[ $1 = 'deploy' ]]; then


    rm -rf .idea/
    rm -rf .vscode/
    rm -rf README.md
    rm -rf kernel/.devcontainer/
    rm -rf kernel/.vscode/

    echo "Frontend: Timofey Moshkara @TimofeyMoshkara | Backend: Adrian Makridenko @lyaguxafrog" > .author

    docker-compose up -d --build 

fi
