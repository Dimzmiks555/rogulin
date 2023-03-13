from django.db import models
from dictionary.models import Company, Trailer, Transport

# Create your models here.

class Firm(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Страховая компания'
        verbose_name_plural = 'Страховые компании'


class Type(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Тип страховки'
        verbose_name_plural = 'Типы страховок'


class Insurance(models.Model):
    open_date = models.DateField('Дата открытия')
    close_date = models.DateField('Дата закрытия')
    
    firm = models.ForeignKey(Firm, verbose_name='Страховая компания', on_delete=models.PROTECT)
    type = models.ForeignKey(Type, verbose_name='Тип', on_delete=models.PROTECT)
    company = models.ForeignKey(Company, verbose_name='Организация', on_delete=models.PROTECT)
    scan = models.ImageField('Скан страховки', default='')
    transport = models.ForeignKey(Transport, verbose_name='Транспорт', blank=True, on_delete=models.PROTECT)
    trailer = models.ForeignKey(Trailer, verbose_name='Прицеп', blank=True, on_delete=models.PROTECT)
    

    class Meta:
        verbose_name = 'Страховка'
        verbose_name_plural = 'Страховки'
