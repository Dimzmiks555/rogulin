# Generated by Django 4.1.4 on 2023-03-13 14:16

from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_ride_from_cities_ride_to_cities_alter_ride_from_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='from_city',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, related_name='from_city', to='dictionary.city', verbose_name='Начальная точка)'),
        ),
        migrations.AddField(
            model_name='ride',
            name='to_city',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, related_name='to_city', to='dictionary.city', verbose_name='Конечная точка)'),
        ),
    ]
