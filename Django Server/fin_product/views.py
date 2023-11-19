from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django.core.exceptions import ObjectDoesNotExist
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
    DepositDebatesSerializer, SavingDebatesSerializer,
    GETDepositOptionsSerializer, GetSavingOptionsSerializer
    )
API_key = settings.API_KEY_FIN_PRD


def update(D_or_S, productserializer, optionserializer, productmodel, optionmodel):
    url = f'http://finlife.fss.or.kr/finlifeapi/{D_or_S}ProductsSearch.json?auth={API_key}&topFinGrpNo=020000&pageNo=1'
    
    try:
        response = requests.get(url).json()
        if response.get('result').get('err_cd') != '000':
            print(response.get('result').get('err_msg'))
            return False, response.get('result').get('err_msg')
    except Exception as e:
        return False, ['금융감독원 OPEN API에서 응답을 받을 수 없거나 올바르지 않은 응답을 받았습니다.', e]

    try:
        for lst in response.get('result').get('baseList'):
            fin_prdt_cd = lst.get('fin_prdt_cd')
            
            try:
                product = productmodel.objects.get(fin_prdt_cd=fin_prdt_cd)
                product_serializer = productserializer(product, data=lst)
            except ObjectDoesNotExist:
                product_serializer = productserializer(data=lst)
            except Exception as e:
                return [False, e]

            if product_serializer.is_valid(raise_exception=True):
                product_serializer.save()

        optionmodel.objects.all().delete()
        for lst in response.get('result').get('optionList'):
            fin_prdt_cd = productmodel.objects.get(fin_prdt_cd=lst.get('fin_prdt_cd'))
            
            try:
                option = optionmodel.objects.get(fin_prdt_cd=fin_prdt_cd, save_trm=lst['save_trm'])
                option_serializer = optionserializer(option, data=lst)
            except ObjectDoesNotExist:   
                option_serializer = optionserializer(data=lst)
            except Exception as e:
                return [False, e]
                
            if option_serializer.is_valid(raise_exception=True):
                option_serializer.save(fin_prdt_cd=fin_prdt_cd)

        return [True]
    except Exception as e:
        return [False, e]

@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly, IsAdminUser])
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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def deposit_options(request, fin_prdt_cd):
    product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    options = get_list_or_404(DepositOptions, fin_prdt_cd=product)
    serializer = GETDepositOptionsSerializer(options, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def saving_options(request, fin_prdt_cd):
    product = get_object_or_404(SavingProducts, fin_prdt_cd=fin_prdt_cd)
    options = get_list_or_404(SavingOptions, fin_prdt_cd=product)
    serializer = GetSavingOptionsSerializer(options, many=True, context={'request':request})
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def deposit_intos(request, option_pk):
    deposit = get_object_or_404(DepositOptions, pk=option_pk)

    is_liked = deposit.into_users.filter(pk=request.user.pk).exists()

    if is_liked:
        deposit.into_users.remove(request.user)
    else:
        deposit.into_users.add(request.user)
            
    like_count = deposit.into_users.aggregate(count=Count('id'))['count']

    data = {
        'isLiked': not is_liked,
        'likeCount': like_count
    }
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def saving_intos(request, option_pk):
    saving = get_object_or_404(SavingOptions, pk=option_pk)

    is_liked = saving.into_users.filter(pk=request.user.pk).exists()

    if is_liked:
        saving.into_users.remove(request.user)
    else:
        saving.into_users.add(request.user)
            
    like_count = saving.into_users.aggregate(count=Count('id'))['count']

    data = {
        'isLiked': not is_liked,
        'likeCount': like_count
    }
    return Response(data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
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
@permission_classes([IsAuthenticatedOrReadOnly])
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