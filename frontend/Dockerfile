
FROM node:18.16.0

ENV APP_ROOT /

WORKDIR ${APP_ROOT}
ADD . ${APP_ROOT}

RUN npm install

RUN npm run build

CMD node .output/server/index.mjs
