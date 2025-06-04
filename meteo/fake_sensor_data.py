import os
import django
import random
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meteo.settings")  # замени на свой проект
django.setup()

from weather.models import Measurement

now = datetime.now()
now = make_aware(now)

for i in range(360):  # 30 точек — по 6 в час, на 5 часов
    ts = now - timedelta(minutes=10 * i)  # шаг 10 минут
    Measurement.objects.create(
        temperature=round(random.uniform(22, 28), 1),
        humidity=round(random.uniform(45, 65), 1),
        pressure=round(random.uniform(755, 770), 1),
        timestamp=ts
    )

print("✅ Данные добавлены.")
