# Инструкция по запуску Django-приложения

1. **Клонируйте репозиторий:**
    ```bash
    git clone <ссылка_на_репозиторий>
    cd meteo_ltpu-master/meteo
    ```

2. **Создайте и активируйте виртуальное окружение:**
    ```bash
    python -m venv venv
    # Для Windows:
    venv\Scripts\activate
    # Для Linux/Mac:
    source venv/bin/activate
    ```

3. **Установите зависимости:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Выполните миграции базы данных:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Запустите сервер разработки:**
    ```bash
    python manage.py runserver
    ```

6. **Откройте приложение в браузере:**
    ```
    http://127.0.0.1:8000/
    ```

**Примечание:**  
Перед запуском убедитесь, что у вас установлен Python и pip.

**Нет метеостанции?**  
Если нет подключенной метеостанции, то нужно создать фейковую информацию  
```bash
python fake_sensor_data.py
```

