from datetime import date

import requests

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Value, Q, Sum
from django.db.models.functions import Coalesce

from .models import UserProfile, Travel
from .serializers import UserProfileSerializer, TravelSerializer, CountrySerializer
from fin_product.models import DepositOptions, SavingOptions
from fin_product.serializers import GETDepositOptionsSerializer, GetSavingOptionsSerializer
from django.conf import settings

API_key = settings.API_KEY_NAVER
secret = settings.NAVER_SECRET

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_info(request):
    if request.method == 'GET':
        profile = get_object_or_404(UserProfile, user=request.user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        profile = get_object_or_404(UserProfile, user=request.user)
        updated_data = request.data.copy()
        
        for field, value in request.data.items():
            if value is None:
                updated_data[field] = getattr(profile, field)

        serializer = UserProfileSerializer(profile,  data=updated_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


def get_top_products_with_options(options_model, group_type, user_profile):
    if group_type == 'likes':
        top_products = options_model.objects.annotate(
        total_into_user=Coalesce(Sum('into_users'), Value(0))
        ).order_by('-total_into_user', '-intr_rate')[:10]
        
    else:
        if getattr(user_profile, f'{group_type}_group') is None:
            return False
        top_products = get_list_or_404(
            options_model.objects.annotate(
                total_into_user=Coalesce(
                    Sum('into_users'),
                    Value(0)
                )
            ).order_by(
                '-total_into_user', '-intr_rate'
            )[:10]
        )
    return top_products

groupe_name = {'age' : '나이', 'monthly_income' : '월 수입', 'assets': '자산'}
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def deposits_recommend(request, group_type):
    if group_type not in {'age', 'monthly_income', 'assets', 'likes'}:
        return Response({'detail':'찾을 수 없는 페이지'},status=status.HTTP_404_NOT_FOUND)
    
    if group_type != 'likes' and not IsAuthenticated:
        return Response({'detail': '회원 정보를 기반으로 추천하는 서비스는 로그인이 필요합니다.'})

    requesting_user_profile = get_object_or_404(UserProfile, user=request.user)

    top_10_liked_deposits = get_top_products_with_options(DepositOptions, group_type, requesting_user_profile)
    if top_10_liked_deposits == False:
        return Response({'detail': f'{groupe_name[group_type]}의 값을 입력하지 않았습니다. 프로필에서 {groupe_name[group_type]}를 입력해주세요'})
    serializer = GETDepositOptionsSerializer(top_10_liked_deposits, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def savings_recommend(request, group_type):
    if group_type not in {'age', 'monthly_income', 'assets', 'likes'}:
        return Response({'detail':'찾을 수 없는 페이지'},status=status.HTTP_404_NOT_FOUND)
    
    if group_type != 'likes' and not IsAuthenticated:
        return Response({'detail': '회원 정보를 기반으로 추천하는 서비스는 로그인이 필요합니다.'})
    
    requesting_user_profile = get_object_or_404(UserProfile, user=request.user)

    top_10_liked_savings = get_top_products_with_options(SavingOptions, group_type, requesting_user_profile)
    if top_10_liked_savings == False:
        return Response({'detail': f'{groupe_name[group_type]}의 값을 입력하지 않았습니다. 프로필에서 {groupe_name[group_type]}를 입력해주세요'})
    serializer = GetSavingOptionsSerializer(top_10_liked_savings, many=True, context={'request': request})
    return Response(serializer.data)



###########################################################################################################################################

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def travel_recommand(request, save_period):
    monthly_saving = int(request.GET.get('monthly_saving', default=False))
    print(monthly_saving)
    if monthly_saving:
        rate = 3
        intr_rate_type = request.GET.get('intr_rate_type', default='S')
        save_period = int(save_period)

        if intr_rate_type == 'S':
            money = (monthly_saving * rate * (save_period+1)*save_period//2)//12
        elif intr_rate_type == 'M':
            money = (monthly_saving*rate*save_period//12)
        
        country = Travel.objects.filter(cost__lt=money).order_by('?')[:5]

        if not country.exists():
            return Response({'detail' : '선택 기간에 적합한 여행지 상품이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TravelSerializer(country, many=True, context={'request':request})
        return Response(serializer.data)

    today = date.today()

    month = today.replace(day=1, month=today.month + 1).month
    date_after_a_month = f',{month},'

    desire_savings_term_options = SavingOptions.objects.filter(save_trm=save_period).order_by('-max_saving_output')[:5]

    if not desire_savings_term_options.exists():
        return Response({'detail' : '선택 기간에 적합한 적금 상품이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        
    maximum_saving_output = desire_savings_term_options[0].max_saving_output // 200
    if save_period == 36:
        maximum_saving_output // 10

    recommend_travel_place = Travel.objects.filter(
        Q(when__contains=date_after_a_month)
        & Q(cost__lte=maximum_saving_output)
    ).order_by('?')
    
    if not recommend_travel_place.exists():
        return Response({'detail' : '선택 기간에 이후에 적합한 여행지가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TravelSerializer(recommend_travel_place, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_saving_for_travel(request, country):

    cost = get_object_or_404(Travel, country=country).cost
    cost //= 10000
    savings_above_cost = SavingOptions.objects.filter(max_saving_output__gt=cost) \
    .order_by('?')[:5]

    if not savings_above_cost.exists():
        return Response({'detail' : '선택 기간에 적합한 적금 상품이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = GetSavingOptionsSerializer(savings_above_cost, many=True, context={'request':request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_country(request):
    countries = get_list_or_404(Travel)
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_img_url(request):
    # return Response({'detail': '이미 완료된 업데이트'})
    countries = get_list_or_404(Travel)

    for country in countries:
        url = f'https://openapi.naver.com/v1/search/image'
        headers = {
            'X-Naver-Client-Id' : API_key,
            'X-Naver-Client-Secret':secret
        }

        params = {
            'query' : f'{country.country}',
            'display': 10,
            'sort':'date',
            'start': 2,
            'filter' : 'medium'
        }
        
        response = requests.get(url, headers=headers, params=params).json()
        print(response)
        country.img_url = response['items'][0]['link']
        country.save()
    
    return Response(status=status.HTTP_201_CREATED)