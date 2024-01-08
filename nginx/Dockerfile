FROM nginx:1.19.0-alpine

RUN apt-get update && \
    apt-get install -y certbot

COPY ./prod.conf /etc/nginx/conf.d/default.conf
