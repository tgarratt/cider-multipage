# Generated by Django 3.0.5 on 2020-07-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20200704_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutuserinfo',
            name='user_price_total',
            field=models.IntegerField(default=0),
        ),
    ]
