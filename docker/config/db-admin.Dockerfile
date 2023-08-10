FROM node:18.15.0

WORKDIR /app

RUN npm install -g dynamodb-admin

CMD ["dynamodb-admin"]