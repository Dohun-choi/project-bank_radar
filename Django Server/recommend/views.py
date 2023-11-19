from datetime import date, timedelta

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Count, Value, Q, Sum
from django.db.models.functions import Coalesce

from .models import UserProfile, Travel
from .serializers import UserProfileSerializer, TravelSerializer
from fin_product.models import DepositOptions, SavingOptions
from fin_product.serializers import DepositOptionsSerializer, GetSavingOptionsSerializer

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


# def get_top_products(product_model, group_type, user_profile):
#     if group_type == 'likes':
#         top_products = get_list_or_404(
#             product_model.objects.annotate(
#                 num_likes=Count('like_users')
#             ).order_by(
#                 '-num_likes', '-max_limit'
#             )[:10]
#         )
#     else:
#         if getattr(user_profile, f'{group_type}_group') is None:
#             return False
#         top_products = get_list_or_404(
#             product_model.objects.annotate(
#                 num_likes=Coalesce(
#                     Count('like_users', filter=Q(
#                         **{f"like_users__userprofile__{group_type}_group": getattr(user_profile, f'{group_type}_group')}
#                     )),
#                     Value(0)
#                 )
#             ).order_by(
#                 '-num_likes', '-max_limit'
#             )[:10]
#         )
#     return top_products

# @api_view(['GET'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def deposits_recommend(request, group_type):
#     if group_type not in {'age', 'monthly_income', 'assets', 'likes'}:
#         return Response({'error': 'Invalid group_type'})
    
#     if group_type != 'likes' and IsAuthenticated:
#         return Response({'detail': '회원 정보를 기반으로 추천하는 서비스는 로그인이 필요합니다.'})

#     requesting_user_profile = get_object_or_404(UserProfile, user=request.user)

#     top_10_liked_deposits = get_top_products(DepositProducts, group_type, requesting_user_profile)
#     if top_10_liked_deposits == False:
#         return Response({'detail': f'{group_type}의 값을 입력하지 않았습니다. 프로필에서 {group_type}를 입력해주세요'})
#     serializer = GETDepositProductsSerializer(top_10_liked_deposits, many=True, context={'request': request})
#     return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def savings_recommend(request, group_type):
#     if group_type not in {'age', 'monthly_income', 'assets', 'likes'}:
#         return Response({'error': 'Invalid group_type'})
    
#     if group_type != 'likes' and IsAuthenticated:
#         return Response({'detail': '회원 정보를 기반으로 추천하는 서비스는 로그인이 필요합니다.'})
    
#     requesting_user_profile = get_object_or_404(UserProfile, user=request.user)

#     if top_10_liked_deposits == False:
#         return Response({'detail': f'{group_type}의 값을 입력하지 않았습니다. 프로필에서 {group_type}를 입력해주세요'})

#     top_10_liked_savings = get_top_products(SavingProducts, group_type, requesting_user_profile)
#     serializer = GETSavingProductsSerializer(top_10_liked_savings, many=True, context={'request': request})
#     return Response(serializer.data)



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

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def deposits_recommend(request, group_type):
    if group_type not in {'age', 'monthly_income', 'assets', 'likes'}:
        return Response({'error': 'Invalid group_type'})
    
    if group_type != 'likes' and IsAuthenticated:
        return Response({'detail': '회원 정보를 기반으로 추천하는 서비스는 로그인이 필요합니다.'})

    requesting_user_profile = get_object_or_404(UserProfile, user=request.user)

    top_10_liked_deposits = get_top_products_with_options(DepositOptions, group_type, requesting_user_profile)
    if top_10_liked_deposits == False:
        return Response({'detail': f'{group_type}의 값을 입력하지 않았습니다. 프로필에서 {group_type}를 입력해주세요'})
    serializer = DepositOptionsSerializer(top_10_liked_deposits, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def savings_recommend(request, group_type):
    if group_type not in {'age', 'monthly_income', 'assets', 'likes'}:
        return Response({'error': 'Invalid group_type'})
    
    if group_type != 'likes' and IsAuthenticated:
        return Response({'detail': '회원 정보를 기반으로 추천하는 서비스는 로그인이 필요합니다.'})
    
    requesting_user_profile = get_object_or_404(UserProfile, user=request.user)

    top_10_liked_savings = get_top_products_with_options(SavingOptions, group_type, requesting_user_profile)
    if top_10_liked_savings == False:
        return Response({'detail': f'{group_type}의 값을 입력하지 않았습니다. 프로필에서 {group_type}를 입력해주세요'})
    serializer = GetSavingOptionsSerializer(top_10_liked_savings, many=True, context={'request': request})
    return Response(serializer.data)



###########################################################################################################################################

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def travel_recommand(request, save_period):
    today = date.today()

    month = today.replace(day=1, month=today.month + 1).month
    date_after_a_month = f',{month},'
    next_recommend = f',{month+1},'

    desire_savings_term_options = SavingOptions.objects.filter(save_trm=save_period).order_by('-max_saving_output')[:5]

    if not desire_savings_term_options.exists():
        return Response({'detail' : '선택 기간에 적합한 적금 상품이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        
    maximum_saving_output = desire_savings_term_options[0].max_saving_output

    recommend_travel_place = Travel.objects.filter(
        (Q(when__contains=date_after_a_month) | Q(when__contains=next_recommend))
        & Q(cost__lte=maximum_saving_output)
    )

    if not recommend_travel_place.exists():
        return Response({'detail' : '선택 기간에 이후에 적합한 여행지가 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TravelSerializer(recommend_travel_place, many=TravelSerializer)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_saving_for_travel(request, country):
    cost = get_object_or_404(Travel, country=country)

    savings_above_cost = SavingOptions.objects.filter(max_saving_output__gt=cost) \
    .order_by('save_trm', 'max_saving_output')[:5]

    if not savings_above_cost.exists():
        return Response({'detail' : '선택 기간에 적합한 적금 상품이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = DepositOptionsSerializer(savings_above_cost, many=True)
    return Response(serializer.data)