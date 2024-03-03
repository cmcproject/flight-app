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
