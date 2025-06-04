import bluetooth
import django
import os
import sys
import datetime

sys.path.append('/home/pi/your_project')  # путь к Django-проекту
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

from weather.models import Measurement

addr = "XX:XX:XX:XX:XX:XX"  # MAC-адрес Arduino
port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((addr, port))

while True:
    data = sock.recv(1024).decode().strip()
    if data:
        try:
            temp, hum, pres = map(float, data.split(","))
            Measurement.objects.create(
                temperature=temp,
                humidity=hum,
                pressure=pres,
                timestamp=datetime.datetime.now()
            )
            print(f"Saved: {temp} {hum} {pres}")
        except ValueError:
            print(f"Invalid data: {data}")
