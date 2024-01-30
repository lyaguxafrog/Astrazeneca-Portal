# Astrazeneca Portal

![Static Badge](https://img.shields.io/badge/Python-%233776AB?style=flat-square&logo=Python&labelColor=yellow) ![Static Badge](https://img.shields.io/badge/Django-%23d0ced0?style=flat-square&logo=django&labelColor=%23092E20&link=https%3A%2F%2Fwww.djangoproject.com%2F) ![Static Badge](https://img.shields.io/badge/Typescript-%233178C6?style=flat-square&logo=Typescript&logoColor=white) ![Static Badge](https://img.shields.io/badge/Nuxt-white?style=flat-square&logo=nuxt.js&logoColor=white&labelColor=%2300DC82) ![Static Badge](https://img.shields.io/badge/PostgreSQL-white?style=flat-square&logo=postgresql&logoColor=white&labelColor=%234169E1) ![Static Badge](https://img.shields.io/badge/Nginx-white?style=flat-square&logo=nginx&logoColor=white&labelColor=%23009639) ![Static Badge](https://img.shields.io/badge/Docker-white?style=flat-square&logo=docker&logoColor=white&labelColor=%232496ED)







### Backend

* Путь: `kernel/`
* Контейнер: `kernel`
* [Стек](https://github.com/lyaguxafrog/portal-backend/blob/release/kernel/requirements.txt):
    * Python v3.9
    * Django v4.2.8
    * DRF v3.14.0
    * Gunicorn v21.2.0
* Readme
* Разработчик: Адриан Макриденко [@lyaguxafrog](https://github.com/lyaguxafrog)

### Frontend

* Путь: `frontend/`
* Контейнер: `nuxt`
* [Стек](https://github.com/lyaguxafrog/portal-backend/blob/release/frontend/package.json):
    * TypeScript v5.0.3
    * Nuxt v3.5.3
* [Readme](https://github.com/lyaguxafrog/portal-backend/blob/release/frontend/README.md)
* Разработчик: Тимофей Мошкара [@TimofeyMoshkara](https://github.com/TimofeyMoshkara)

### Web-server

* Путь: `nginx/prod.conf`
* Контейнер: `nginx`
* Image: [nginx-certbot](https://hub.docker.com/r/staticfloat/nginx-certbot)
* Стек:
    * Nginx v1.19.10
    * Certbot

### Database

* Путь: `db/`
* Права доступа: `drwx------`
* Контейнер: `db`
* Image: [postgres](https://hub.docker.com/_/postgres)
* Стек:
    * PostgreSQL: latest

## Other

* Docker
* Docker-compose v3.7


## Config & Deploy

1. Для конфигурации приложения выполните команду:
```bash
./helper.sh config
```

Сконфигурируется новый файлы `kernel/.env` со следующим наполнением:
```

                    # ОБЯЗАТЕЛЬНО СМЕНИТЬ!
SECRET_KEY = "61vw)!727arcolu$ah%*53jlzju(f#9ogwna0u(apx0gl#0%=x" # Секретный ключ для шифорвания
ADMIN_PASSWORD = "admin" # Пароль пользователя admin, создается при первом запуске


# True - запустить приложение в режиме отладки, нужно для разработки
DEBUG_FLAG = "False"

SSO_URL = "https://sso.az.clients.dobroagency.ru"

OUR_DOMAIN = "" # домен на котором будет развернуто приложение

SSO_OUR_DOMAIN = "example.com"
SSO_REDIRECT_DOMAIN = "example.com"

# не трогать
POSTGRES_USER = "developer"
POSTGRES_DB = "db"
POSTGRES_PASSWORD = "Passw0rd33"

```
* `SECRET_KEY` - Секретный ключ для шифрования файлов и API запросов. **ОБЯЗАТЕЛЬНО СМЕНИТЬ**
* `ADMIN_PASSWORD` - Пароль пользователя `admin` в админ-панели, пользователь создается **только** при первом деплое, далее пароль останется таким, каким Вы его задали. **ОБЯЗАТЕЛЬНО СМЕНИТЬ**
* `DEBUG_FLAG` - При деплое оставить `False`.
* `SSO_URL` - URL для редиректа при работе SSO.
* `OUR_DOMAIN` - Домен приложения.
* `SSO_OUR_DOMAIN` - Домен откуда происходит редирект при работе SOO.
* `SSO_REDIRECT_DOMAIN` - Домен куда будет редирект при работе SSO.
* `POSTGRES_USER`, `POSTGRES_DB`, `POSTGRES_PASSWORD` - Поля, которые не нужно изменять, для смены проконсультируйтесь с разработчиком.


Заполните и измените новые поля.

2.  Деплой приложения используйте команду:
```bash
./helper.sh deploy
```


