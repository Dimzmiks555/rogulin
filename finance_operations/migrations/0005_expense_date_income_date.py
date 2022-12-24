# Generated by Django 4.1.4 on 2022-12-23 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "finance_operations",
            "0004_rename_passport_date_worksheet_close_date_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="expense",
            name="date",
            field=models.DateField(
                default=datetime.date(2022, 12, 23), verbose_name="Дата"
            ),
        ),
        migrations.AddField(
            model_name="income",
            name="date",
            field=models.DateField(
                default=datetime.date(2022, 12, 23), verbose_name="Дата"
            ),
        ),
    ]