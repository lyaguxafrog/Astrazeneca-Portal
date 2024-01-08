#!/bin/sh
set -e

certbot certonly --webroot -w /var/www/certbot -d astraportal.dev-demo.online

exec "$@"
