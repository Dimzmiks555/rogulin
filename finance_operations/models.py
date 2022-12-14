from django.db import models
from common.models import ExpenseType, IncomeType

# Create your models here.


# Расход
class Expense(models.Model):
    summ = models.DecimalField('Сумма', max_digits=20, decimal_places=2)
    type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE, verbose_name='Тип')
    
    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'

# Доход
class Income(models.Model):
    summ = models.DecimalField('Сумма', max_digits=20, decimal_places=2)
    type = models.ForeignKey(IncomeType, on_delete=models.CASCADE, verbose_name='Тип')
    
    class Meta:
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'

