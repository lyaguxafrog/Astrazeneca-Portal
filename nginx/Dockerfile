FROM nginx:1.19.0-alpine

# Install Certbot
RUN apk add --no-cache certbot

# Copy Nginx configuration
COPY ./prod.conf /etc/nginx/conf.d/default.conf

# Install Supervisor
RUN apk add --no-cache supervisor

# Copy Supervisor configuration
COPY supervisord.conf /etc/supervisord.conf

# Expose ports
EXPOSE 80
EXPOSE 443

# Start Supervisor
CMD ["supervisord", "-c", "/etc/supervisord.conf"]
