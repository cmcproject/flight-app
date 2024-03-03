"""
URL mappings for the flight API
"""
from django.urls import path

from flight import views

app_name = "flight"

urlpatterns = [
    path("sensor-data/", views.SensorDataAPIView.as_view(), name="sensor-data"),
]
