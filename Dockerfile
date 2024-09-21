# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.10.0

FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py migrate
# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD gunicorn 'django_project.wsgi' --bind=0.0.0.0:8000
