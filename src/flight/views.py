from rest_framework import generics, mixins, status, views, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import serializers
from .models import FlightRoute, SensorDataAnalysis, Waypoint
from .serializers import SensorDataAnalysisSerializer


class SensorDataAPIView(generics.GenericAPIView):
    """
    Sensor data
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SensorDataAnalysisSerializer

    def get_queryset(self):
        # TODO: link data to user
        # user = self.request.user
        qs = SensorDataAnalysis.objects.all().order_by("-id")
        return qs

    def get_serializer_class(self):
        return self.serializer_class

    def get(self, request, *args, **kwargs):
        """
        Get team information
        """
        qs = self.get_queryset()
        if qs:
            serializer = self.get_serializer(qs.first())
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(
            data={"msg": "Sensor data not available"},
            status=status.HTTP_404_NOT_FOUND,
        )


class FlightRouteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FlightRouteSerializer
    queryset = FlightRoute.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by("-id").distinct()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WaypointViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.WaypointSerializer
    queryset = Waypoint.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(user=self.request.user).order_by("-name").distinct()


class MostUsedFlightRouteAPIView(views.APIView):
    """
    Most used flight route
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Get most used flight route
        """
        return Response(
            data={"msg": "TO BE IMPLEMENTED"},
            status=status.HTTP_200_OK,
        )


class MostEfficientFlightRouteAPIView(views.APIView):
    """
    Most efficient flight route
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Get most effieicnet flight route
        """
        return Response(
            data={"msg": "TO BE IMPLEMENTED"},
            status=status.HTTP_200_OK,
        )
