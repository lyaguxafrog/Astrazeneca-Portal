FROM nginx:1.19.0-alpine

RUN apk update && \
    apk add certbot

COPY ./prod.conf /etc/nginx/conf.d/default.conf

# Добавляем конфигурацию для Certbot
COPY ./nginx.conf /etc/nginx/nginx.conf

# Копируем entrypoint скрипт, который будет выполнять Certbot
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
