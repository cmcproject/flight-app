"""
URL mappings for the flight API
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from flight import views

app_name = "flight"

router = DefaultRouter()
router.register("flight-routes", views.FlightRouteViewSet, "flight-routes")
router.register("waypoints", views.WaypointViewSet, "waypoints")


urlpatterns = [
    path("sensor-data/", views.SensorDataAPIView.as_view(), name="sensor-data"),
    path("", include(router.urls)),
    path(
        "most-used-flight-route/",
        views.MostUsedFlightRouteAPIView.as_view(),
        name="most-used-flight-route",
    ),
    path(
        "most-efficient-flight-route/",
        views.MostEfficientFlightRouteAPIView.as_view(),
        name="most-efficient-flight-route",
    ),
]
