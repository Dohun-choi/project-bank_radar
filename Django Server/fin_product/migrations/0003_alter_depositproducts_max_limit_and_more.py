# Generated by Django 4.2.4 on 2023-11-17 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin_product', '0002_remove_depositproducts_wish_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositproducts',
            name='max_limit',
            field=models.IntegerField(default='-1', null=True),
        ),
        migrations.AlterField(
            model_name='savingproducts',
            name='max_limit',
            field=models.IntegerField(default=-1, null=True),
        ),
    ]
