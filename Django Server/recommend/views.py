from datetime import date, timedelta

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Count, Value, Q
from django.db.models.functions import Coalesce

from .models import UserProfile
from .serializers import UserProfileSerializer
from fin_product.models import DepositProducts, SavingProducts
from fin_product.serializers import GETDepositProductsSerializer, GETSavingProductsSerializer

@api_view(['GET', 'PUT'])
@login_required
def user_info(request):
    if request.method == 'GET':
        profile = get_object_or_404(UserProfile, user=request.user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        profile = get_object_or_404(UserProfile, user=request.user)
        serializer = UserProfileSerializer(profile,  data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
@login_required
def deposits_recommend(request, group_type):
    if group_type not in {'age', 'monthly_income', 'assets', 'likes'}:
        return Response({'error': 'Invalid group_type'})

    requesting_user_profile = get_object_or_404(UserProfile, user=request.user)
    
    if group_type == 'likes':
        top_10_liked_deposits = get_list_or_404(
            DepositProducts.objects.annotate(
                num_likes=Count('like_users')
            ).order_by(
                '-num_likes', '-max_limit'
            )[:10]
        )

    else:
        top_10_liked_deposits = get_list_or_404(
            DepositProducts.objects.annotate(
                num_likes=Coalesce(
                    Count('like_users', filter=Q(
                        **{f"like_users__userprofile__{group_type}_group": getattr(requesting_user_profile, f'{group_type}_group')}
                    )),
                    Value(0)
                )
            ).order_by(
                '-num_likes', '-max_limit'
            )[:10]
        )

    serializer = GETDepositProductsSerializer(top_10_liked_deposits, many=True, context={'request':request})

    return Response(serializer.data)


@api_view(['GET'])
@login_required
def savings_recommend(request, group_type):
    if group_type not in {'age', 'monthly_income', 'assets', 'likes'}:
        return Response({'error': 'Invalid group_type'})

    requesting_user_profile = get_object_or_404(UserProfile, user=request.user)
    
    if group_type == 'likes':
        top_10_liked_savings = get_list_or_404(
            SavingProducts.objects.annotate(
                num_likes=Count('like_users')
            ).order_by(
                '-num_likes', '-max_limit'
            )[:10]
        )

    else:
        top_10_liked_savings = get_list_or_404(
            SavingProducts.objects.annotate(
                num_likes=Coalesce(
                    Count('like_users', filter=Q(
                        **{f"like_users__userprofile__{group_type}_group": getattr(requesting_user_profile, f'{group_type}_group')}
                    )),
                    Value(0)
                )
            ).order_by(
                '-num_likes', '-max_limit'
            )[:10]
        )

    serializer = GETSavingProductsSerializer(top_10_liked_savings, many=True, context={'request':request})

    return Response(serializer.data)


@api_view(['GET'])
@login_required
def travel_recommand(request, save_period):
    today = date.today()

    date_after_a_month = today + timedelta(days=30)
