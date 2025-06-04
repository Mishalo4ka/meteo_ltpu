from django.db import models

# Create your models here.
class Measurement(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp}: T={self.temperature} H={self.humidity} P={self.pressure}"
