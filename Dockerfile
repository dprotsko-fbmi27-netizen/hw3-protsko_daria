# Базовий образ
FROM python:3.11-slim

# Робоча директорія
WORKDIR /app

# Копіюємо файли
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Команда запуску
CMD ["python", "app.py"]