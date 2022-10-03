FROM php:8.0.5-fpm-alpine

RUN adduser -D php8

# RUN apt update && apt install -y \
#     git \
#     curl \
#     zip \
#     unzip

# RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
USER php8

WORKDIR /var/www/html

COPY --chown=php8:php8 . .

# RUN chown php8:php8 ./cache


EXPOSE 5000
