FROM python:3.9.10
# setting crontab
    # COPY crontab /etc/cron.d/crontab
    # RUN chmod 0644 /etc/cron.d/crontab
    # RUN touch /var/log/cron.log
    # RUN apt-get update && \
    #         apt-get install cron -y
    # RUN cron && tail -f /var/log/cron.log

# setting main flask before
    # RUN adduser anonim
    # WORKDIR /home/anonim
    # RUN mkdir ./kalkulator_GKSK
    # COPY --chown=root:root ./main/*.py ./kalkulator_GKSK/
    # RUN mkdir ./kalkulator_GKSK/templates
    # COPY --chown=root:root ./main/templates/* ./kalkulator_GKSK/templates/
    # USER anonim
    # RUN pip3 install --upgrade pip
    # RUN pip3 install --user --no-cache-dir flask
    # CMD ["python3","./kalkulator_GKSK/main_web.py"]

RUN adduser anonim
WORKDIR /home/anonim
COPY --chown=root:root ./main/*.py ./
RUN mkdir ./templates
COPY --chown=root:root ./main/templates/* ./templates/
RUN chmod 0644 ./*.py
RUN chmod 0644 ./templates/*
USER anonim
RUN pip3 install --upgrade pip
RUN pip3 install --user --no-cache-dir flask

ENV FLASK_APP=/main/main_web.py
ENV FLASK_RUN_HOST=0.0.0.0

# CMD ["python3","./main_web.py"]
CMD ["python3","-m","flask","run"]