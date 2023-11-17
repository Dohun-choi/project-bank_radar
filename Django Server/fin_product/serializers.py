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
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)
    is_liked = serializers.SerializerMethodField(method_name='has_liked', read_only=True)

    class Meta:
        model = SavingProducts
        fields = '__all__'
        read_only_fields = ('like_users',)

    def has_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.like_users.filter(id=request.user.id).exists()
        return False

class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd',)


class GETDepositProductsSerializer(serializers.ModelSerializer):
    options = DepositOptionsSerializer(many=True, read_only=True)
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)
    is_liked = serializers.SerializerMethodField(method_name='has_liked', read_only=True)

    class Meta:
        model = DepositProducts
        fields = '__all__'
        read_only_fields = ('like_users',)
    
        
    def has_liked(self, obj):
        request = self.context.get('request')
        print(self.context)
        if request and request.user.is_authenticated:
            return obj.like_users.filter(id=request.user.id).exists()
        return False


class GETSavingProductsSerializer(serializers.ModelSerializer):
    options = SavingOptionsSerializer(many=True, read_only=True)
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)
    is_liked = serializers.SerializerMethodField(method_name='has_liked', read_only=True)

    class Meta:
        model = DepositProducts
        fields = '__all__'
        read_only_fields = ('like_users',)
    
    def has_liked(self, obj):
        request = self.context.get('request')
        print(self.context)
        if request and request.user.is_authenticated:
            return obj.like_users.filter(id=request.user.id).exists()
        return False


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