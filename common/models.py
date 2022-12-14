from django.db import models

# Create your models here.

# Тип дохода
class IncomeType(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Тип доход'
        verbose_name_plural = 'Типы доходов'

    
    def __str__(self):
        return self.name


# Тип расхода
class ExpenseType(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Тип расхода'
        verbose_name_plural = 'Типы расходов'

    
    def __str__(self):
        return self.name
