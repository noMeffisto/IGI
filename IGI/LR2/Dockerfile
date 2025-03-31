# Базовый образ с Python
FROM python:3.9-slim

# Установка рабочей директории
WORKDIR /app

# Копирование папки geometric_lib
COPY geometric_lib/ ./geometric_lib/

# Копирование скрипта
COPY script.py .

# Указание команды для запуска скрипта
CMD ["python", "script.py"]