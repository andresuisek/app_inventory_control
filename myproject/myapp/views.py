from rest_framework import generics
from .models import Humidity, Temperature
from .serializers import HumiditySerializer, TemperatureSerializer


class HumidityListCreateView(generics.ListCreateAPIView):
    queryset = Humidity.objects.all().order_by("-date")
    serializer_class = HumiditySerializer


class TemperatureListCreateView(generics.ListCreateAPIView):
    queryset = Temperature.objects.all().order_by("-date")
    serializer_class = TemperatureSerializer
