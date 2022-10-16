FROM python:3.9.5

RUN adduser anonim
WORKDIR /home/anonim
COPY --chown=root:root ./*.py ./
RUN mkdir ./templates
COPY --chown=root:root ./templates/* ./templates/
RUN chmod 0644 ./*.py
RUN chmod 0644 ./templates/*
USER anonim
RUN pip3 install --upgrade pip
RUN pip3 install --user --no-cache-dir flask

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=21202
ENV FLASK_DEBUG=False

CMD ["python3","-m","flask","run"]