# Generated by Django 3.0.4 on 2020-04-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default=84957777777, max_length=11, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.IntegerField(verbose_name='Почтовый индекс'),
        ),
    ]
