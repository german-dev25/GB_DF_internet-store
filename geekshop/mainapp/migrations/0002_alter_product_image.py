# Generated by Django 3.2.11 on 2022-01-25 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products', verbose_name='картинка'),
        ),
    ]
