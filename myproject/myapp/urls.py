from django.urls import path
from .views import HumidityListCreateView, TemperatureListCreateView

urlpatterns = [
    path("humidity/", HumidityListCreateView.as_view(), name="humidity-list-create"),
    path(
        "temperature/",
        TemperatureListCreateView.as_view(),
        name="temperature-list-create",
    ),
]
