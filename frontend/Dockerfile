
FROM node:16.17.0

ENV APP_ROOT /web

WORKDIR ${APP_ROOT}
ADD . ${APP_ROOT}

RUN npm install

COPY . .

RUN npm run build:test

COPY . .

CMD npm run start
