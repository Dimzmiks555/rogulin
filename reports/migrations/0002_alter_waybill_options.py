# Generated by Django 4.1.4 on 2022-12-23 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='waybill',
            options={'verbose_name': 'Путевой лист', 'verbose_name_plural': 'Путевые листы'},
        ),
    ]