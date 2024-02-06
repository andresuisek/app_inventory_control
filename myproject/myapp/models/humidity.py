from django.db import models


class Humidity(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    value = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=30, null=True, blank=True, default="%")
