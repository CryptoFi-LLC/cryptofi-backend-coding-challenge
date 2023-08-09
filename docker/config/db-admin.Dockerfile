version: '3.8'
name: cws-fi-onboarding
services:
  cws-fi-onboarding:
    container_name: cws-fi-onboarding
    build:
      context: ../..
      dockerfile: local/config/Dockerfile
    ports:
      - "8000:80"
    volumes:
      - ../../src/api:/app/api
      - ../../local:/app/local
      - ../../test:/app/test
    depends_on: 
      - db
      - motoserver
    env_file:
      - ../env/.env
      - ../env/.env.secret

  db:
    image: amazon/dynamodb-local
    container_name: db
    command: "-jar DynamoDBLocal.jar -port 8003 -sharedDb -optimizeDbBeforeStartup -dbPath /home/dynamodblocal/data/"
    ports:
      - 8003:8003
    user: root
    volumes:
      - dynamodb_data:/home/dynamodblocal/data

  db-admin:
    container_name: db-admin
    build:
      context: .
      dockerfile: db-admin.Dockerfile
    ports:
      - 8001:8001
    environment:
      - DYNAMO_ENDPOINT=http://db:8003
    depends_on:
      - db

volumes:
  dynamodb_data: null