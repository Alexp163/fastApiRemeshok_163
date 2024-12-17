# обозначаем  операционную систему для разработки
FROM python:3.12-slim

# обозначаем папку для приложения
WORKDIR /app

# копируем содержимое в рабочую папку
COPY . .

# программа для установки requirements
RUN pip install -r requirements.txt

# указываем папку src(для вызова приложения из src)
WORKDIR /app/src

# запуск приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
