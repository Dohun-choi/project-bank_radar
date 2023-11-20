from rest_framework import serializers
from django.db.models import Count
from .models import (
    DepositProducts, DepositOptions,
    SavingProducts, SavingOptions,
    DepositDebate, SavingDebate
    )

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd', 'into_users',)


class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'


class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd', 'into_users',)


class GETDepositProductsSerializer(serializers.ModelSerializer):
    into_count = serializers.SerializerMethodField(method_name='get_into_count', read_only=True)

    class Meta:
        model = DepositProducts
        fields = '__all__'

    def get_into_count(self, obj):
        return DepositOptions.objects.filter(fin_prdt_cd=obj).aggregate(count=Count('into_users'))['count']



class GETSavingProductsSerializer(serializers.ModelSerializer):
    into_count = serializers.SerializerMethodField(method_name='get_into_count', read_only=True)

    class Meta:
        model = SavingProducts
        fields = '__all__'

    def get_into_count(self, obj):
        return SavingOptions.objects.filter(fin_prdt_cd=obj).aggregate(count=Count('into_users'))['count']



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


class GetSavingOptionsSerializer(serializers.ModelSerializer):
    into_count = serializers.IntegerField(source='into_users.count', read_only=True)
    is_into = serializers.SerializerMethodField(method_name='is_joined', read_only=True)
    kor_co_nm = serializers.CharField(source='fin_prdt_cd.kor_co_nm', read_only=True)
    fin_prdt_nm = serializers.CharField(source='fin_prdt_cd.fin_prdt_nm', read_only=True)

    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd', 'into_users', 'max_saving_output', )

    def is_joined(self, obj):
        request = self.context.get('request')
        return obj.into_users.filter(id=request.user.id).exists()



class GETDepositOptionsSerializer(serializers.ModelSerializer):
    into_count = serializers.IntegerField(source='into_users.count', read_only=True)
    is_into = serializers.SerializerMethodField(method_name='is_joined', read_only=True)
    kor_co_nm = serializers.CharField(source='fin_prdt_cd.kor_co_nm', read_only=True)
    fin_prdt_nm = serializers.CharField(source='fin_prdt_cd.fin_prdt_nm', read_only=True)

    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('fin_prdt_cd', 'into_users', )

    def is_joined(self, obj):
        request = self.context.get('request')
        return obj.into_users.filter(id=request.user.id).exists()