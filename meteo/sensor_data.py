import os
import django
import serial
from datetime import datetime
from django.utils.timezone import make_aware

# Указываем настройки Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meteo.settings")
django.setup()

from weather.models import Measurement

ser = serial.Serial(
    port='/dev/rfcomm0', # замените на ваш порт
    baudrate=38400, # скорость передачи данных
)

print("🚀 Сбор информации с метеостанции запущен")



try:
    while True:
        line = ser.readline().decode().strip()
        data =list(map(float, line.split()))
        temperature = round(data[0], 1)
        humidity = round(data[1], 1)
        pressure = round(data[2])

        timestamp = make_aware(datetime.now())

        # Сохраняем в базу
        Measurement.objects.create(
            temperature=temperature,
            humidity=humidity,
            pressure=pressure,
            timestamp=timestamp
        )

        print(f"📥 Добавлено: {temperature}°C, {humidity}%, {pressure} мм рт. ст.")

except KeyboardInterrupt:
    print("⛔ Остановка")

