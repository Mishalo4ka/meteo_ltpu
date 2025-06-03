from django.shortcuts import render
from .models import Measurement
from django.utils.timezone import now, timedelta


# Create your views here.
def dashboard(request):
    latest = Measurement.objects.last()

    # Данные за последние 12 часов с шагом 30 минут
    cutoff = now() - timedelta(hours=12)
    measurements = Measurement.objects.filter(timestamp__gte=cutoff).order_by('timestamp')

    # Группировка с интервалом 30 минут
    labels = []
    temperatures = []
    humidities = []
    pressures = []

    interval = timedelta(minutes=30)
    t = cutoff
    while t <= now():
        point = measurements.filter(timestamp__gte=t, timestamp__lt=t + interval)
        if point.exists():
            avg_temp = sum(p.temperature for p in point) / point.count()
            avg_hum = sum(p.humidity for p in point) / point.count()
            avg_pres = sum(p.pressure for p in point) / point.count()
        else:
            avg_temp = avg_hum = avg_pres = None

        labels.append(t.strftime("%H:%M"))
        temperatures.append(round(avg_temp, 1) if avg_temp is not None else None)
        humidities.append(round(avg_hum, 1) if avg_hum is not None else None)
        pressures.append(round(avg_pres, 1) if avg_pres is not None else None)

        t += interval

    return render(request, 'weather/dashboard.html', {
        'latest': latest,
        'labels': labels,
        'temperatures': temperatures,
        'humidities': humidities,
        'pressures': pressures,
    })
