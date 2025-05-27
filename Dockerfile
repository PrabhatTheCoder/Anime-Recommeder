# Base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /anime_recommender

RUN apt-get update && apt-get install -y gcc libpq-dev

COPY requirements.txt /anime_recommender/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /anime_recommender/

EXPOSE 8000


CMD ["./entrypoints.sh"]