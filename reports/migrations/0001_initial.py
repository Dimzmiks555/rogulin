# Generated by Django 4.1.4 on 2023-01-03 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('finance_operations', '0001_initial'),
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WayBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_date', models.DateField()),
                ('close_date', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.company', verbose_name='Организация')),
                ('worksheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance_operations.worksheet', verbose_name='Рабочий лист')),
            ],
            options={
                'verbose_name': 'Путевой лист',
                'verbose_name_plural': 'Путевые листы',
            },
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('distance', models.IntegerField(verbose_name='Расстояние')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city', to='dictionary.city', verbose_name='Начальная точка')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_city', to='dictionary.city', verbose_name='Конечная точка')),
                ('waybill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.waybill', verbose_name='Путевой лист')),
            ],
            options={
                'verbose_name': 'Рейс',
                'verbose_name_plural': 'Рейсы',
            },
        ),
    ]
