# Generated by Django 4.1.4 on 2023-01-04 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_operations', '0002_worksheet_tonnage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(default=datetime.date(2023, 1, 4), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=datetime.date(2023, 1, 4), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='mileage',
            field=models.IntegerField(default=0, verbose_name='Пробег, км'),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='tonnage',
            field=models.IntegerField(default=0, verbose_name='Тоннаж, т'),
        ),
    ]