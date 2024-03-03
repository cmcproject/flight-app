from rest_framework import serializers

from .models import SensorDataAnalysis


class SensorDataAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorDataAnalysis
        fields = "__all__"
