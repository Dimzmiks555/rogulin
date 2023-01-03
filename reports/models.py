from django.db import models
from finance_operations.models import WorkSheet
from dictionary.models import City, Company, Doctor, Engineer

# Create your models here.


class WayBill(models.Model):

    open_date=models.DateField()
    close_date=models.DateField()
    worksheet=models.ForeignKey(WorkSheet, on_delete=models.CASCADE, verbose_name='Рабочий лист')
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Врач', null=True)
    engineer=models.ForeignKey(Engineer, on_delete=models.CASCADE, verbose_name='Механик', null=True)
    company=models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Организация')

    class Meta:
        verbose_name="Путевой лист"
        verbose_name_plural="Путевые листы"

    
    def __str__(self) :
        return f'Путевой лист № {self.id}'


class Ride(models.Model):

    date=models.DateField()
    waybill=models.ForeignKey(WayBill, on_delete=models.CASCADE, verbose_name='Путевой лист')
    distance=models.IntegerField('Расстояние')
    from_city=models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city', verbose_name='Начальная точка')
    to_city=models.ForeignKey(City, on_delete=models.CASCADE, related_name='to_city', verbose_name='Конечная точка')

    class Meta:
        verbose_name="Рейс"
        verbose_name_plural="Рейсы"

    
    def __str__(self) :
        return f'Рейс {self.from_city} - {self.to_city}'