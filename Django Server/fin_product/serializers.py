from rest_framework import serializers
from .models import (
    DepositProducts, DepositOptions,
    SavingProducts, SavingOptions,
    DepositDebate, SavingDebate
    )

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'
        read_only_fields = ('like_users',)


class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd',)


class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'
        read_only_fields = ('like_users',)


class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd',)


class GETDepositProductsSerializer(serializers.ModelSerializer):
    options = DepositOptionsSerializer(many=True, read_only=True)
    class Meta:
        model = DepositProducts
        fields = '__all__'
        read_only_fields = ('like_users',)


class GETSavingProductsSerializer(serializers.ModelSerializer):
    options = SavingOptionsSerializer(many=True, read_only=True)
    class Meta:
        model = DepositProducts
        fields = '__all__'
        read_only_fields = ('like_users',)


class DepositDebatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositDebate
        fields = '__all__'
        read_only_fields = ('user', 'fin_prdt_cd')


class SavingDebatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingDebate
        fields = '__all__'
        read_only_fields = ('user', 'fin_prdt_cd')