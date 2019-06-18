FROM python:3.7-slim

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1
RUN apt update
RUN apt-get install -y postgresql-common libpq-dev python3-dev gcc

RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -w 4 -b 0.0.0.0:8080 wsgi
