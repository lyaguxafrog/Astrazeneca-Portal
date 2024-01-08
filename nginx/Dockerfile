FROM nginx:1.19.0-alpine

RUN apk update && \
    apk add certbot

COPY ./prod.conf /etc/nginx/conf.d/default.conf
