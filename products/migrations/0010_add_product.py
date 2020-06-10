# Generated by Django 3.0.5 on 2020-06-10 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_add_bottle_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('1', 'Bottle'), ('2', 'Crate'), ('3', 'Keg')], default='', max_length=50)),
                ('product_title', models.CharField(max_length=50)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_img', models.ImageField(blank=True, null=True, upload_to='static/img/bottle')),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
