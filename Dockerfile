# tag image as logisticasur-img:1.0
FROM python:3.9-alpine

COPY ./LogisticaSur /app/.

WORKDIR /app/LogisticaSur

RUN pip install -r requeriments.txt