from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import SensorDataAnalysis
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
