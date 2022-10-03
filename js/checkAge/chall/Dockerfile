FROM node:16-alpine

RUN adduser -D anonim

WORKDIR /home/anonim

COPY . .

RUN npm install

USER anonim

EXPOSE 20202

CMD [ "npm", "start"]