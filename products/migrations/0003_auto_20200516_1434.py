# Generated by Django 3.0.5 on 2020-05-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200515_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_bottle',
            name='bottle_img',
            field=models.ImageField(blank=True, null=True, upload_to='../../static/img/cider-bottle-template.png'),
        ),
        migrations.AlterField(
            model_name='add_crate',
            name='crate_img',
            field=models.ImageField(blank=True, null=True, upload_to='../../static/img/cider-bottle-template.png'),
        ),
        migrations.AlterField(
            model_name='add_keg',
            name='keg_img',
            field=models.ImageField(blank=True, null=True, upload_to='../../static/img/cider-bottle-template.png'),
        ),
    ]