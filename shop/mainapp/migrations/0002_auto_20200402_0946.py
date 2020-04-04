# Generated by Django 3.0.4 on 2020-04-02 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='picture',
            options={'ordering': ('title',), 'verbose_name': 'Картинка', 'verbose_name_plural': 'Картинки'},
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Цена'),
        ),
    ]
