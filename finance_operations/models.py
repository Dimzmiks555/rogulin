from django.db import models
from common.models import ExpenseType, IncomeType
from dictionary.models import Transport, Employee, Trailer
from datetime import date

# Create your models here.


# Рабочий лист
class WorkSheet(models.Model):
    open_date = models.DateField('Дата открытия', default=date.today)
    close_date = models.DateField('Дата закрытия', default=date.today)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, verbose_name='Транспорт')
    trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE, verbose_name='Прицеп', default=None)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Работник')
    mileage = models.IntegerField('Пробег', default=0)
    
    class Meta:
        verbose_name = 'Рабочий лист'
        verbose_name_plural = 'Рабочие листы'

    
    def __str__(self) :
        return f'Путевой лист {self.id}'


# Расход
class Expense(models.Model):
    date = models.DateField('Дата', default=date.today())
    summ = models.DecimalField('Сумма', max_digits=20, decimal_places=2)
    type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE, verbose_name='Тип')
    work_sheet = models.ForeignKey(WorkSheet, on_delete=models.CASCADE, verbose_name='Рабочий лист', default=0)
    
    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'

# Доход
class Income(models.Model):
    date = models.DateField('Дата', default=date.today())
    summ = models.DecimalField('Сумма', max_digits=20, decimal_places=2)
    type = models.ForeignKey(IncomeType, on_delete=models.CASCADE, verbose_name='Тип')
    work_sheet = models.ForeignKey(WorkSheet, on_delete=models.CASCADE, verbose_name='Рабочий лист', default=0)
    
    class Meta:
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'
