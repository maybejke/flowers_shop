# Generated by Django 3.0.4 on 2020-04-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20200404_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='products', to='mainapp.Category', verbose_name='Категории'),
        ),
    ]
