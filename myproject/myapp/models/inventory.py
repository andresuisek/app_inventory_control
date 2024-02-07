from django.db import models


class Inventory(models.Model):
    last_update = models.DateTimeField()
    product_key = models.CharField(max_length=50, null=True, blank=True)
    product_label = models.CharField(max_length=50, null=True, blank=True)
    product_quantity = models.IntegerField(null=True, blank=True)
