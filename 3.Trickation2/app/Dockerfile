FROM php:7.4-apache
RUN chmod 755 -R /var/www/html
RUN adduser anonim
USER anonim
COPY --chown=anonim:anonim ./app/* /var/www/html
COPY ./config/php.ini /usr/local/etc/php/php.ini
# COPY --chown=anonim:anonim ./index.php /var/www/html