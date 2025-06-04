from django.shortcuts import render
from .models import Measurement
from django.utils.timezone import now, timedelta

def dashboard_old(request):
    latest = Measurement.objects.last()

    cutoff = now() - timedelta(hours=3)
    measurements = Measurement.objects.filter(timestamp__gte=cutoff).order_by('timestamp')

    interval = timedelta(minutes=30)
    t = cutoff

    labels = []
    pressures = []
    temperatures = []
    humidities = []

    while t <= now():
        points = measurements.filter(timestamp__gte=t, timestamp__lt=t + interval)
        if points.exists():
            avg_temp = sum(p.temperature for p in points) / points.count()
            avg_hum = sum(p.humidity for p in points) / points.count()
            avg_pres = sum(p.pressure for p in points) / points.count()
        else:
            avg_temp = avg_hum = avg_pres = None

        labels.append(t.strftime("%H:%M"))
        temperatures.append(round(avg_temp, 1) if avg_temp else None)
        humidities.append(round(avg_hum, 1) if avg_hum else None)
        pressures.append(round(avg_pres, 1) if avg_pres else None)

        t += interval

    return render(request, 'weather/dashboard.html', {
        'latest': latest,
        'labels': labels,
        'temperatures': temperatures,
        'humidities': humidities,
        'pressures': pressures,
    })

def dashboard(request):
    latest = Measurement.objects.last()
    measurements = Measurement.objects.order_by('-timestamp')[:12][::-1]
    labels = [m.timestamp.strftime("%H:%M") for m in measurements]
    temperatures = [m.temperature for m in measurements]
    humidities = [m.humidity for m in measurements]
    pressures = [m.pressure for m in measurements]




    return render(request, 'weather/dashboard.html', {
        'latest': latest,
        'labels': labels,
        'temperatures': temperatures,
        'humidities': humidities,
        'pressures': pressures,
    })