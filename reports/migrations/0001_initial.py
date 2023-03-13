# Generated by Django 4.1.4 on 2023-03-13 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dictionary', '0001_initial'),
        ('finance_operations', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='WayBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_date', models.DateField()),
                ('close_date', models.DateField()),
                ('comment', models.TextField(default=None, null=True, verbose_name='Комментарий')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.company', verbose_name='Организация')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dictionary.doctor', verbose_name='Врач')),
                ('engineer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dictionary.engineer', verbose_name='Механик')),
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
                ('distance', models.IntegerField(verbose_name='Расстояние, км')),
                ('ttn_number', models.CharField(default='', max_length=255, verbose_name='№ ТТН')),
                ('cargo_name', models.CharField(default='', max_length=255, verbose_name='Название груза')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city', to='dictionary.city', verbose_name='Начальная точка')),
                ('orderer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dictionary.company', verbose_name='Заказчик')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_city', to='dictionary.city', verbose_name='Конечная точка')),
                ('waybill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.waybill', verbose_name='Путевой лист')),
            ],
            options={
                'verbose_name': 'Рейс',
                'verbose_name_plural': 'Рейсы',
            },
        ),
    ]
