from rest_framework import serializers
from myapp.models import Humidity, Temperature


class HumiditySerializer(serializers.ModelSerializer):
    key = serializers.SerializerMethodField()
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Humidity
        fields = "__all__"

    def get_key(self, obj):
        return obj.id


class TemperatureSerializer(serializers.ModelSerializer):
    key = serializers.SerializerMethodField()
    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Temperature
        fields = "__all__"

    def get_key(self, obj):
        return obj.id
