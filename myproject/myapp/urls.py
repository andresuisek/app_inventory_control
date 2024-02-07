from django.urls import path

from .views import InventoryListCreateView, InventoryHistoricalListCreateView

urlpatterns = [
    path("inventory/", InventoryListCreateView.as_view(), name="inventory-list-create"),
    path(
        "inventory_historical/",
        InventoryHistoricalListCreateView.as_view(),
        name="inventory-historical-list-create",
    ),
    # path("humidity/", HumidityListCreateView.as_view(), name="humidity-list-create"),
    # path(
    #     "temperature/",
    #     TemperatureListCreateView.as_view(),
    #     name="temperature-list-create",
    # ),
]
