# Generated by Django 4.2.4 on 2023-11-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_notify_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=1500),
        ),
    ]
