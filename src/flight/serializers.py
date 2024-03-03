from rest_framework import serializers

from .models import FlightRoute, SensorDataAnalysis, Waypoint


class SensorDataAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorDataAnalysis
        fields = "__all__"


class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = "__all__"
        read_only_fields = ["id"]


class FlightRouteSerializer(serializers.ModelSerializer):
    waypoints = WaypointSerializer(many=True, required=False)

    class Meta:
        model = FlightRoute
        fields = "__all__"
        read_only_fields = ["id"]

    def _get_or_create_waypoints(self, waypoints, flight_route):
        auth_user = self.context["request"].user
        for waypoint in waypoints:
            waypoint_obj, _ = Waypoint.objects.get_or_create(
                user=auth_user,
                **waypoint,
            )
            flight_route.waypoints.add(waypoint_obj)

    def create(self, validated_data):
        waypoints = validated_data.pop("waypoints", [])

        flight_route = FlightRoute.objects.create(**validated_data)
        self._get_or_create_waypoints(waypoints, flight_route)

        return flight_route

    def update(self, instance, validated_data):
        waypoints = validated_data.pop("waypoints", None)

        if waypoints is not None:
            instance.waypoints.clear()
            self._get_or_create_waypoints(waypoints, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance
