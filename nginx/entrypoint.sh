#!/bin/sh
set -e

sleep "${WAIT_FOR_NUXT:-10}"

certbot certonly --webroot -w /var/www/certbot -d astraportal.dev-demo.online --email maccree.a@yandex.ru --agree-tos --non-interactive --force-renewal

exec "$@"
