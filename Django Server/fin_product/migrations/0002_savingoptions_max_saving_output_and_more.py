# Generated by Django 4.2.4 on 2023-11-18 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin_product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='savingoptions',
            name='max_saving_output',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='savingoptions',
            name='save_trm',
            field=models.SmallIntegerField(default=0, null=True),
        ),
    ]