# Generated by Django 3.0.5 on 2020-07-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20200708_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutuserinfo',
            name='user_price_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
