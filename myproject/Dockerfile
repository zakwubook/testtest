FROM python:3.11-slim

# Установите необходимые зависимости для установки Google Chrome
RUN apt-get update && apt-get install -y \
    wget \
    libnss3 \
    libgconf-2-4 \
    && rm -rf /var/lib/apt/lists/*

# Скачайте и установите Google Chrome
RUN wget -nc https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

WORKDIR /usr/src/wubook

ENV PYTHONBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .