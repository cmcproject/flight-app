from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models


class SensorDataAnalysis(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    initial_entries = models.IntegerField(default=0)
    entries_after_cleanup = models.IntegerField(default=0)
    test_locations = models.IntegerField(default=0)
    start_location = models.CharField(max_length=200)
    end_location = models.CharField(max_length=200)
    intermediate_locations = ArrayField(
        models.CharField(max_length=200),
        default=list,
    )

    def __str__(self) -> str:
        return f"{self.start_location} ' -> ' {self.end_location}"


class FlightRoute(models.Model):
    """Flight route object"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    models.DurationField
    date = models.DateTimeField()
    duration = models.DurationField()
    airline = models.CharField(max_length=255)
    aircraft = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    fuel_consumption = models.DecimalField(max_digits=5, decimal_places=2)
    waypoints = models.ManyToManyField("Waypoint")

    def __str__(self):
        return f"{self.airline} {self.aircraft} {self.origin} -> {self.destination}"


class Waypoint(models.Model):
    """Waypoint object"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    wind_direction = models.DecimalField(max_digits=5, decimal_places=2)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    latitude = models.DecimalField(max_digits=5, decimal_places=2)
    longitude = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
