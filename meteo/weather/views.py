from django.shortcuts import render
from .models import Measurement
from django.http import JsonResponse


def dashboard(request):
    latest = Measurement.objects.last()
    measurements = Measurement.objects.order_by("-timestamp")[:6][::-1]
    labels = [m.timestamp.strftime("%H:%M") for m in measurements]
    temperatures = [m.temperature for m in measurements]
    humidities = [m.humidity for m in measurements]
    pressures = [m.pressure for m in measurements]

    return render(
        request,
        "weather/dashboard.html",
        {
            "latest": latest,
            "labels": labels,
            "temperatures": temperatures,
            "humidities": humidities,
            "pressures": pressures,
        },
    )


def latest_data(request):
    latest = Measurement.objects.last()
    if latest:
        return JsonResponse(
            {
                "temperature": latest.temperature,
                "humidity": latest.humidity,
                "pressure": latest.pressure,
                "timestamp": latest.timestamp.strftime("%H:%M:%S"),
            }
        )
    return JsonResponse({}, status=404)
