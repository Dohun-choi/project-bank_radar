from rest_framework import serializers
from .models import ExchangeInfo

class ExchangeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExchangeInfo
        fields = '__all__'