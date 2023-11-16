from django.db import models
from django.conf import settings


class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)                      # 금융 상품 코드
    dcls_month = models.IntegerField(null=True, default='알수 없음')  # 공시 제출 월
    kor_co_nm = models.TextField(null=True, default='알수 없음')      # 금융 회사명
    fin_prdt_nm = models.TextField(null=True, default='알수 없음')    # 금융 상품명
    etc_note = models.TextField(null=True, default='정보 없음')       # 금융 상품 설명
    join_deny = models.IntegerField(null=True, default=-1)           # 가입 제한(1: 제한 없음, 2: 서민전용, 3:일부제한)
    join_member = models.TextField(null=True, default='알수 없음')    # 가입 대상
    join_way = models.TextField(null=True, default='알수 없음')       # 가입 방법
    max_limit = models.IntegerField(null=True, default='정보 없음')   # 최고한도
    spcl_cnd = models.TextField(null=True, default='알수 없음')       # 우대 조건
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_deposit')


class DepositOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(DepositProducts, related_name='options', on_delete=models.CASCADE)                  # 금융 상품 코드
    intr_rate_type = models.TextField(null=True, default='알수 없음')                           # 저축 금리 유형
    intr_rate_type_nm = models.CharField(null=True, max_length=100, default='알수 없음')        # 저축금리 유형명
    intr_rate = models.FloatField(null=True, default=-1)                                       # 저축금리
    intr_rate2 = models.FloatField(null=True, default=-1)                                      # 최고우대금리
    save_trm = models.SmallIntegerField(null=True, default=-1)                                 # 저축기간(단위:개월)


class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)                      # 금융 상품 코드
    dcls_month = models.IntegerField(null=True, default='알수 없음')  # 공시 제출 월
    kor_co_nm = models.TextField(null=True, default='알수 없음')      # 금융 회사명
    fin_prdt_nm = models.TextField(null=True, default='알수 없음')    # 금융 상품명
    etc_note = models.TextField(null=True, default='정보 없음')       # 금융 상품 설명
    join_deny = models.IntegerField(null=True, default=-1)           # 가입 제한(1: 제한 없음, 2: 서민전용, 3:일부제한)
    join_member = models.TextField(null=True, default='알수 없음')    # 가입 대상
    join_way = models.TextField(null=True, default='알수 없음')       # 가입 방법
    max_limit = models.IntegerField(null=True, default='정보 없음')   # 최고한도
    spcl_cnd = models.TextField(null=True, default='알수 없음')       # 우대 조건
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_saving')


class SavingOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(SavingProducts, related_name='options', on_delete=models.CASCADE)# 금융 상품 코드
    intr_rate_type = models.TextField(null=True, default='알수 없음')                           # 저축 금리 유형
    intr_rate_type_nm = models.CharField(null=True, max_length=100, default='알수 없음')        # 저축금리 유형명
    intr_rate = models.FloatField(null=True, default=-1)                                       # 저축금리
    intr_rate2 = models.FloatField(null=True, default=-1)                                      # 최고우대금리
    save_trm = models.SmallIntegerField(null=True, default=-1)                                 # 저축기간(단위:개월)