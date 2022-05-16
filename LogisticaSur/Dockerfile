# tagged image as logisticasur-img:1.0
FROM python:3.8-slim-buster

RUN apt-get update && apt-get install python3-dev default-libmysqlclient-dev build-essential -y

WORKDIR /app

COPY requeriments.txt .

RUN pip install -r requeriments.txt

COPY . .

EXPOSE 8080
