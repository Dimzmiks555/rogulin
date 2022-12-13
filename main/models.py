from django.db import models

# Create your models here.

# Транспорт
class Transport(models.Model):
    reg_number = models.CharField('Регистрационный номер', max_length=20)



# Работник
class Employee(models.Model):
    sur_name = models.CharField('Фамилия', max_length=255)
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Отчество', max_length=255)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

# Тип расхода
class ExpenseType(models.Model):
    name = models.CharField('Название', max_length=255)

# Расход
class Expense(models.Model):
    summ = models.DecimalField('Сумма', max_digits=20, decimal_places=2)
    type = models.ForeignKey('Тип', ExpenseType, on_delete=models.CASCADE)

# Тип дохода
class IncomeType(models.Model):
    name = models.CharField('Название', max_length=255)

# Доход
class Income(models.Model):
    summ = models.DecimalField('Сумма', max_digits=20, decimal_places=2)
    type = models.ForeignKey('Тип', IncomeType, on_delete=models.CASCADE)

