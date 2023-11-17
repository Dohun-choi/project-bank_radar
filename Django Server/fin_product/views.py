from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Count

from django.conf import settings
from .models import (
    DepositProducts, SavingProducts,
    DepositOptions, SavingOptions,
    DepositDebate, SavingDebate
    )
from .serializers import (
    DepositProductsSerializer, DepositOptionsSerializer,
    SavingProductsSerializer, SavingOptionsSerializer,
    GETDepositProductsSerializer, GETSavingProductsSerializer,
    DepositDebatesSerializer, SavingDebatesSerializer
    )
API_key = settings.API_KEY_FIN_PRD


def update(D_or_S, productserializer, optionserializer, productmodel, optionmodel):
    url = f'http://finlife.fss.or.kr/finlifeapi/{D_or_S}ProductsSearch.json?auth={API_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    if response.get('result').get('err_cd') != '000':
        print(response.get('result').get('err_msg'))
        return False, response.get('result').get('err_msg')

    try:
        for lst in response.get('result').get('baseList'):
            fin_prdt_cd = lst.get('fin_prdt_cd')
            
            try:
                product = productmodel.objects.get(fin_prdt_cd=fin_prdt_cd)
                product_serializer = productserializer(product, data=lst)
            except productmodel.DoesNotExist:
                product_serializer = productserializer(data=lst)

            if product_serializer.is_valid(raise_exception=True):
                product_serializer.save()

        optionmodel.objects.all().delete()
        for lst in response.get('result').get('optionList'):
            option_serializer = optionserializer(data=lst)
            if option_serializer.is_valid(raise_exception=True):
                fin_prdt_cd = productmodel.objects.get(fin_prdt_cd=lst.get('fin_prdt_cd'))
                option_serializer.save(fin_prdt_cd=fin_prdt_cd)

        return True, True
    except:
        return False, '알 수 없는 에러'

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_product(request):
    deposit_updated = update('deposit', DepositProductsSerializer, DepositOptionsSerializer, DepositProducts, DepositOptions)
    saving_updated = update('saving', SavingProductsSerializer, SavingOptionsSerializer, SavingProducts, SavingOptions)
    if deposit_updated[0] and saving_updated[0]:
        return Response(status=status.HTTP_201_CREATED)
    return Response({'detail': f'적금 갱신: {saving_updated[1]}\예금 갱신: {deposit_updated[1]}'}, status=status.HTTP_502_BAD_GATEWAY)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_from_DB(request):
    data = get_list_or_404(DepositProducts)
    serializer = GETDepositProductsSerializer(data, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saving_from_DB(request):
    data = get_list_or_404(SavingProducts)
    serializer = GETSavingProductsSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deposit_likes(request, fin_prdt_cd):
    deposit = get_object_or_404(DepositProducts, pk=fin_prdt_cd)

    is_liked = deposit.like_users.filter(pk=request.user.pk).exists()

    if is_liked:
        deposit.like_users.remove(request.user)
    else:
        deposit.like_users.add(request.user)
            
    like_count = deposit.like_users.aggregate(count=Count('id'))['count']

    data = {
        'isLiked': not is_liked,
        'likeCount': like_count
    }
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def saving_likes(request, fin_prdt_cd):
    saving = get_object_or_404(SavingProducts, pk=fin_prdt_cd)

    is_liked = saving.like_users.filter(pk=request.user.pk).exists()

    if is_liked:
        saving.like_users.remove(request.user)
    else:
        saving.like_users.add(request.user)
            
    like_count = saving.like_users.aggregate(count=Count('id'))['count']

    data = {
        'isLiked': not is_liked,
        'likeCount': like_count
    }
    return Response(data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def deposit_debate(request, fin_prdt_cd):
    if request.method == 'GET':
        data = get_list_or_404(DepositDebate, fin_prdt_cd=fin_prdt_cd)
        serializer = DepositDebatesSerializer(data, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepositDebatesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            deposit = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
            serializer.save(fin_prdt_cd=deposit, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def saving_debate(request, fin_prdt_cd):
    if request.method == 'GET':
        data = get_list_or_404(SavingDebate, fin_prdt_cd=fin_prdt_cd)
        serializer = SavingDebatesSerializer(data, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SavingDebatesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            saving = get_object_or_404(SavingProducts, fin_prdt_cd=fin_prdt_cd)
            serializer.save(fin_prdt_cd=saving, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)