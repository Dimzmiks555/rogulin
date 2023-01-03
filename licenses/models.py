from django.db import models
from dictionary.models import Company, Trailer, Transport

# Create your models here.

class Firm(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Фирма'


class Type(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Тип'


class Insurance(models.Model):
    open_date = models.DateField('Дата открытия')
    close_date = models.DateField('Дата закрытия')
    firm = models.ForeignKey(Firm, verbose_name='Фирма', on_delete=models.CASCADE)
    type = models.ForeignKey(Type, verbose_name='Тип', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, verbose_name='Организация', on_delete=models.CASCADE)
    transport = models.ForeignKey(Transport, verbose_name='Транспорт', blank=True, on_delete=models.CASCADE)
    trailer = models.ForeignKey(Trailer, verbose_name='Прицеп', blank=True, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = 'Страховка'
        verbose_name_plural = 'Страховки'
