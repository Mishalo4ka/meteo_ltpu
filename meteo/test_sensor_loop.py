# test_sensor_loop.py

import os
import django
import random
import time
from datetime import datetime
from django.utils.timezone import make_aware

# Указываем настройки Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meteo.settings")  # замени на своё имя проекта
django.setup()

from weather.models import Measurement

print("🚀 Тестовая симуляция метеостанции запущена...")

try:
    while True:
        # Случайные значения
        temperature = round(random.uniform(20.0, 30.0), 1)
        humidity = round(random.uniform(40.0, 70.0), 1)
        pressure = round(random.uniform(750.0, 770.0), 1)

        timestamp = make_aware(datetime.now())

        # Сохраняем в базу
        Measurement.objects.create(
            temperature=temperature,
            humidity=humidity,
            pressure=pressure,
            timestamp=timestamp
        )

        print(f"📥 Добавлено: {temperature}°C, {humidity}%, {pressure} мм рт. ст.")

        # Ждём 5 секунд
        time.sleep(5)

except KeyboardInterrupt:
    print("⛔ Остановка симуляции вручную.")
