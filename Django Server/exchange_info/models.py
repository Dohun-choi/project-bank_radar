from django.db import models

class ExchangeInfo(models.Model):
    cur_unit = models.TextField(primary_key=True) # 통화 코드
    cur_nm = models.TextField() # 국가/통화명
    deal_bas_r = models.TextField() # 매매 기준율