from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_list_or_404

from django.conf import settings
from .models import (
    DepositProducts, SavingProducts,
    DepositOptions, SavingOptions
    )
from .serializers import (
    DepositProductsSerializer, DepositOptionsSerializer,
    SavingProductsSerializer, SavingOptionsSerializer,
    GETDepositProductsSerializer, GETSavingProductsSerializer
    )
API_key = settings.API_KEY_FIN_PRD


def update(D_or_S, productserializer, optionserializer, productmodel, optionmodel):
    url = f'http://finlife.fss.or.kr/finlifeapi/{D_or_S}ProductsSearch.json?auth={API_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    if not response or not response.get('result'):
        return False
    productmodel.objects.all().delete()
    optionmodel.objects.all().delete()
    try:
        for lst in response.get('result').get('baseList'):
            product_serializer = productserializer(data=lst)
            if product_serializer.is_valid(raise_exception=True):
                product_serializer.save()
        
        for lst in response.get('result').get('optionList'):
            option_serializer = optionserializer(data=lst)
            if option_serializer.is_valid(raise_exception=True):
                fin_prdt_cd = productmodel.objects.get(fin_prdt_cd=lst.get('fin_prdt_cd'))
                option_serializer.save(fin_prdt_cd=fin_prdt_cd)

        return True
    except:
        return False

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_product(request):
    deposit_updated = update('deposit', DepositProductsSerializer, DepositOptionsSerializer, DepositProducts, DepositOptions)
    saving_updated = update('saving', SavingProductsSerializer, SavingOptionsSerializer, SavingProducts, SavingOptions)
    if deposit_updated and saving_updated:
        return Response(status=status.HTTP_201_CREATED)
    return Response({'detail': f'적금 갱신: {saving_updated}\예금 갱신: {deposit_updated}'}, status=status.HTTP_502_BAD_GATEWAY)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_from_DB(request):
    data = get_list_or_404(DepositProducts)
    serializer = GETDepositProductsSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saving_from_DB(request):
    data = get_list_or_404(DepositProducts)
    serializer = GETSavingProductsSerializer(data, many=True)
    return Response(serializer.data)