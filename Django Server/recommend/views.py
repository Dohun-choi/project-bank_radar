from rest_framework.response import Response
from django.db.models import Count

from .models import UserProfile
from fin_product.models import DepositProducts


def user_info(request):
    pass


def deposits_recommend():
    users_by_age_ordered_by_wishes = UserProfile.objects.annotate(
        age_group=DepositProducts.F('age') // 10
    ).values('age_group').annotate(
        total_likes=Count('wish_users')
    ).order_by('-total_likes')

    context = {
        'users_by_age_ordered_by_likes': users_by_age_ordered_by_wishes
    }

    return Response(context)


def savings_recommend():
    pass