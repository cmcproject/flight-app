# Generated by Django 5.0 on 2024-03-03 07:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: list = []

    operations = [
        migrations.CreateModel(
            name="SensorDataAnalysis",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("initial_entries", models.IntegerField(default=0)),
                ("entries_after_cleanup", models.IntegerField(default=0)),
                ("test_locations", models.IntegerField(default=0)),
                ("start_location", models.CharField(max_length=200)),
                ("end_location", models.CharField(max_length=200)),
                (
                    "intermediate_locations",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=200), default=list, size=None
                    ),
                ),
            ],
        ),
    ]