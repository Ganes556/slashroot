FROM php:8.0.5-fpm-alpine

RUN adduser -D php8

RUN apt-get update && apt-get install -y \
    git \
    curl \
    zip \
    unzip

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

WORKDIR /var/www

# RUN chown php8:php8 ./cache

# COPY --chown=php8:php8 . .
COPY --chown=root:php8 . .







