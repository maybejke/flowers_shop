# Generated by Django 3.0.4 on 2020-04-28 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0009_auto_20200418_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_time',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Желаемое время доставки'),
        ),
    ]
