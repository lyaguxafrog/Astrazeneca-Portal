#!/bin/sh
set -e

certbot certonly --webroot -w /var/www/certbot -d astraportal.dev-demo.online --email maccree.a@yandex.ru --agree-tos

exec "$@"
