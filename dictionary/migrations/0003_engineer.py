# Generated by Django 4.1.4 on 2023-01-03 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_doctor'),
    ]

    operations = [
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
    ]
