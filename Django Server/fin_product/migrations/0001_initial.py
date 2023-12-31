# Generated by Django 4.2.4 on 2023-11-21 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositProducts',
            fields=[
                ('fin_prdt_cd', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('dcls_month', models.IntegerField(default='알수 없음', null=True)),
                ('kor_co_nm', models.TextField(default='알수 없음', null=True)),
                ('fin_prdt_nm', models.TextField(default='알수 없음', null=True)),
                ('etc_note', models.TextField(default='정보 없음', null=True)),
                ('join_deny', models.IntegerField(default=-1, null=True)),
                ('join_member', models.TextField(default='알수 없음', null=True)),
                ('join_way', models.TextField(default='알수 없음', null=True)),
                ('max_limit', models.IntegerField(default='-1', null=True)),
                ('spcl_cnd', models.TextField(default='알수 없음', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavingProducts',
            fields=[
                ('fin_prdt_cd', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('dcls_month', models.IntegerField(default='알수 없음', null=True)),
                ('kor_co_nm', models.TextField(default='알수 없음', null=True)),
                ('fin_prdt_nm', models.TextField(default='알수 없음', null=True)),
                ('etc_note', models.TextField(default='정보 없음', null=True)),
                ('join_deny', models.IntegerField(default=-1, null=True)),
                ('join_member', models.TextField(default='알수 없음', null=True)),
                ('join_way', models.TextField(default='알수 없음', null=True)),
                ('max_limit', models.IntegerField(default=-1, null=True)),
                ('spcl_cnd', models.TextField(default='알수 없음', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavingOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intr_rate_type', models.TextField(default='알수 없음', null=True)),
                ('intr_rate_type_nm', models.CharField(default='알수 없음', max_length=100, null=True)),
                ('intr_rate', models.FloatField(default=-1, null=True)),
                ('intr_rate2', models.FloatField(default=-1, null=True)),
                ('save_trm', models.SmallIntegerField(default=0, null=True)),
                ('max_saving_output', models.FloatField(default=0)),
                ('fin_prdt_cd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='fin_product.savingproducts')),
                ('into_users', models.ManyToManyField(related_name='into_saving_options', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavingDebate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('fin_prdt_cd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='fin_product.savingproducts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_on_savings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DepositOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intr_rate_type', models.TextField(default='알수 없음', null=True)),
                ('intr_rate_type_nm', models.CharField(default='알수 없음', max_length=100, null=True)),
                ('intr_rate', models.FloatField(default=-1, null=True)),
                ('intr_rate2', models.FloatField(default=-1, null=True)),
                ('save_trm', models.SmallIntegerField(default=-1, null=True)),
                ('fin_prdt_cd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='fin_product.depositproducts')),
                ('into_users', models.ManyToManyField(related_name='into_deposit_options', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DepositDebate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('fin_prdt_cd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='fin_product.depositproducts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_on_deposits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
