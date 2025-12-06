# Используем официальный образ Python
FROM python:3.11-slim

# Установка рабочего каталога в контейнере
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Команда запуска определяется в docker-compose.yml
