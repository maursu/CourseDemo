# Используем базовый образ Python
FROM python:3.11-slim

# Устанавливаем переменную окружения PYTHONUNBUFFERED в значение 1
# Это гарантирует, что вывод Python не будет буферизоваться
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /code

# Устанавливаем зависимости через pip
COPY requirements/requirements-prod.txt /code/
RUN pip install --no-cache-dir -r requirements-prod.txt

# Копируем файлы проекта в рабочую директорию контейнера
COPY . /code/
