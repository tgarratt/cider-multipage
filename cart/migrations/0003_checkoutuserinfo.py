# Generated by Django 3.0.5 on 2020-07-04 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20200610_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutUserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=30, verbose_name='E-mail')),
                ('user_name', models.CharField(max_length=60, verbose_name='Full name')),
                ('user_country', models.CharField(max_length=60, verbose_name='Country')),
                ('user_city', models.CharField(max_length=60, verbose_name='City')),
                ('user_line1', models.CharField(max_length=60, verbose_name='Address line 1')),
                ('user_line2', models.CharField(max_length=60, verbose_name='Address line 2')),
                ('user_postcode', models.CharField(max_length=60, verbose_name='Postcode')),
                ('user_countystate', models.CharField(max_length=60, verbose_name='County/State')),
            ],
        ),
    ]
