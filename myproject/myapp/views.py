from rest_framework import generics
from myapp.models import Inventory, InventoryHistorical

from .serializers import InventorySerializer, InventoryHistoricalSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException

class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all().order_by("-last_update")
    serializer_class = InventorySerializer


class InventoryHistoricalListCreateView(generics.ListCreateAPIView):
    queryset = InventoryHistorical.objects.all().order_by("-date")
    serializer_class = InventoryHistoricalSerializer

    def create(self, request, *args, **kwargs):
        inventory = Inventory.objects.filter(id=1).last()
        if not inventory:
            raise APIException()
        
        data = request.data.copy()
        data.appendlist('inventory', inventory.id) 

        if data['type_register'] == 'Entry':
            value = inventory.product_quantity + 1
            inventory.product_quantity = value
            inventory.save()
            data['quantity'] = value
        else:
            value = inventory.product_quantity - 1
            if value < 0:
                value = 0
            inventory.product_quantity = value
            inventory.save()
            data['quantity'] = value

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
