from django.db import models
from finance_operations.models import WorkSheet
from dictionary.models import City, Company, Doctor, Engineer

# Create your models here.


class WayBill(models.Model):

    open_date=models.DateField('Дата открытия')
    close_date=models.DateField('Дата закрытия')
    worksheet=models.ForeignKey(WorkSheet, on_delete=models.PROTECT, verbose_name='Рабочий лист')
    doctor=models.ForeignKey(Doctor, on_delete=models.PROTECT, verbose_name='Врач', null=True)
    engineer=models.ForeignKey(Engineer, on_delete=models.PROTECT, verbose_name='Механик', null=True)
    company=models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='Организация')
    comment=models.TextField(verbose_name='Комментарий', default=None, null=True, blank=True)

    class Meta:
        verbose_name="Путевой лист"
        verbose_name_plural="Путевые листы"

    
    def __str__(self) :
        return f'Путевой лист № {self.id}'


class Ride(models.Model):

    date=models.DateField()
    waybill=models.ForeignKey(WayBill, on_delete=models.PROTECT, verbose_name='Путевой лист')
    distance=models.IntegerField('Расстояние, км')
    ttn_number=models.CharField('№ ТТН', max_length=255, default='')
    cargo_name=models.CharField('Название груза', max_length=255, default='')
    from_city=models.ForeignKey(City, on_delete=models.PROTECT, related_name='from_city', verbose_name='Начальная точка)', blank=True, default=None)
    to_city=models.ForeignKey(City, on_delete=models.PROTECT, related_name='to_city', verbose_name='Конечная точка)', blank=True, default=None)
    from_cities=models.ManyToManyField(City, related_name='from_cities', verbose_name='Начальные точки', blank=True, default=None)
    to_cities=models.ManyToManyField(City, related_name='to_cities', verbose_name='Конечные точки', blank=True, default=None)
    orderer=models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='Заказчик', default=None)

    class Meta:
        verbose_name="Рейс"
        verbose_name_plural="Рейсы"

    
    def __str__(self) :
        return f'Рейс {self.from_city} - {self.to_city}'