from rest_framework import serializers
from .models import UserProfile, Travel
from fin_product.serializers import SavingOptionsSerializer, DepositOptionsSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    into_deposits = DepositOptionsSerializer(many=True, read_only=True)
    into_savings = SavingOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'