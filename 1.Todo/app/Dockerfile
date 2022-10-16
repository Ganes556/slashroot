FROM python:latest

RUN adduser anonim
WORKDIR /home/anonim

COPY . .
RUN chown anonim:anonim ./todos

USER anonim
RUN pip3 install --upgrade pip
RUN pip3 install --user --no-cache-dir flask

ENV FLASK_APP=app.py
ENV FLASK_RUN_PORT=21201
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=True

EXPOSE 21201


CMD ["python","-m","flask","run"]
