from django.urls import path
from .views import dashboard, latest_data

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('latest/', latest_data, name='latest_data'),
]
