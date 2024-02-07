from django.db import models

from myapp.models import Inventory


class InventoryHistorical(models.Model):
    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    quantity = models.IntegerField(null=True, blank=True)
    type_register = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
