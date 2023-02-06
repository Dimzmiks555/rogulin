# Generated by Django 4.1.4 on 2023-01-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0006_transport_sts_scan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='driving_license_scan',
            field=models.ImageField(blank=True, default='', upload_to='', verbose_name='Скан водительского удостоверения'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='passport_scan',
            field=models.ImageField(blank=True, default='', upload_to='', verbose_name='Скан паспорта'),
        ),
    ]