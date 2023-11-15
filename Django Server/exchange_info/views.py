from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser

from django.conf import settings
from .serializers import ExchangeSerializers
from .models import ExchangeInfo
API_key = settings.API_KEY_EXCHANGE

@permission_classes([IsAdminUser])
@api_view(['GET'])
def renew_exchange_info(request):

    ExchangeInfo.objects.all().delete()

    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_key}&data=AP01'
    response = requests.get(url).json()

    for li in response:
        save_data = {
            'cur_unit': li.get('cur_unit'),
            'cur_nm': li.get('cur_nm'),
            'deal_bas_r': li.get('deal_bas_r')
            }
        serializer = ExchangeSerializers(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def exchange_from_DB(request):
    data = ExchangeInfo.objects.all()
    serializer = ExchangeSerializers(data, many=True)
    return Response(serializer.data)