from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_list_or_404

from django.conf import settings
from .serializers import ExchangeSerializers
from .models import ExchangeInfo
API_key = settings.API_KEY_EXCHANGE
API_ERROR = {2 : 'DATA코드 오류', 3 : '인증코드 오류', 4 : '일일제한횟수 마감'}

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_exchange_DB(request):
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_key}&data=AP01'
    response = requests.get(url).json()
    if not response:
        return Response({"detail": "환율 정보 갱신 실패"})
    ExchangeInfo.objects.all().delete()

    for li in response:
        if li.get('result') != 1:
            return Response({'detail': f'한국수출입 은행 OPEN API 오류 : {API_ERROR[li.get("result")]}'})
        serializer = ExchangeSerializers(data=li)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def exchange_from_DB(request):
    data = get_list_or_404(ExchangeInfo)
    serializer = ExchangeSerializers(data, many=True)
    return Response(serializer.data)