#!/bin/bash


if [[ $1 = 'config' ]]; then

    rm -rf .idea/
    rm -rf .vscode/
    rm -rf README.md
    rm -rf kernel/.devcontainer/
    rm -rf kernel/.vscode/
    rm -rf kernel/README.md

    mkdir kernel/logs
    mkdir frontend/dist
    
    cat .env.example >> kernel/.env
    echo ".env создан"
    echo "Обязательно смените SECRET_KEY и ADMIN_PASSWORD"   
    
fi

if [[ $1 = 'deploy' ]]; then


    echo "Frontend: Timofey Moshkara @TimofeyMoshkara | Backend: Adrian Makridenko @lyaguxafrog" > .author

    docker-compose up -d --build 
    # clear
    echo "Deployed!"
fi

if [[ $1 = 'update' ]]; then

	git stash
	git pull
	docker-compose up -d --build
	docker system prune -af
	clear
	exit 0
    
fi
