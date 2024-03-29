# Generated by Django 4.1.4 on 2023-03-13 08:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Название')),
                ('region', models.CharField(default='', max_length=255, verbose_name='Регион')),
                ('area', models.CharField(default='', max_length=255, verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(default='', help_text='Обязательно вводить через пробел!', max_length=255, verbose_name='ФИО')),
                ('inn', models.CharField(default='', max_length=255, verbose_name='ИНН')),
                ('ogrn', models.CharField(default='', max_length=255, verbose_name='ОГРН')),
                ('address', models.CharField(default='', max_length=255, verbose_name='Юридический адрес')),
                ('phone', models.CharField(default='', max_length=255, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sur_name', models.CharField(default='', max_length=255, verbose_name='Фамилия')),
                ('first_name', models.CharField(default='', max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(default='', max_length=255, verbose_name='Отчество')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врач',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sur_name', models.CharField(default='', max_length=255, verbose_name='Фамилия')),
                ('first_name', models.CharField(default='', max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(default='', max_length=255, verbose_name='Отчество')),
                ('passport_number', models.CharField(default='', max_length=255, verbose_name='Серия и номер паспорта')),
                ('passport_date', models.DateField(default=datetime.date.today, verbose_name='Дата выдачи')),
                ('passport_given_by', models.CharField(default='', max_length=255, verbose_name='Выдан (кем?)')),
                ('passport_filial_code', models.CharField(default='', max_length=20, verbose_name='Код подразделения')),
                ('passport_address', models.CharField(default='', max_length=255, verbose_name='Адрес прописки')),
                ('driving_license', models.CharField(default='', max_length=255, verbose_name='Номер водительского удостоверения')),
                ('passport_scan', models.FileField(blank=True, default='', upload_to='', verbose_name='Скан паспорта')),
                ('driving_license_scan', models.FileField(blank=True, default='', upload_to='', verbose_name='Скан водительского удостоверения')),
                ('phone', models.CharField(default='', max_length=255, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sur_name', models.CharField(default='', max_length=255, verbose_name='Фамилия')),
                ('first_name', models.CharField(default='', max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(default='', max_length=255, verbose_name='Отчество')),
            ],
            options={
                'verbose_name': 'Механик',
                'verbose_name_plural': 'Механик',
            },
        ),
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Название')),
                ('reg_number', models.CharField(default='', max_length=255, verbose_name='Регистрационный номер')),
            ],
            options={
                'verbose_name': 'Прицеп',
                'verbose_name_plural': 'Прицепы',
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Название')),
                ('model', models.CharField(default='', max_length=255, verbose_name='Модель')),
                ('reg_number', models.CharField(max_length=20, verbose_name='Регистрационный номер')),
                ('mileage', models.IntegerField(blank=True, default=0, verbose_name='Пробег')),
                ('sts_number', models.CharField(blank=True, default='', max_length=100, verbose_name='Номер СТС')),
                ('sts_scan', models.FileField(blank=True, default='', upload_to='', verbose_name='Скан СТС')),
                ('pts_number', models.CharField(blank=True, default='', max_length=100, verbose_name='Номер ПТС')),
                ('vin', models.CharField(blank=True, default='', max_length=100, verbose_name='VIN-Номер')),
            ],
            options={
                'verbose_name': 'Транспорт',
                'verbose_name_plural': 'Транспорт',
            },
        ),
    ]
