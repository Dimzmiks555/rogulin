from django.db import models
from finance_operations.models import WorkSheet

# Create your models here.


class WayBill(models.Model):

    open_date=models.DateField()
    close_date=models.DateField()
    worksheet=models.ForeignKey(WorkSheet, on_delete=models.CASCADE, verbose_name='Рабочий лист')

    class Meta:
        verbose_name="Путевой лист"
        verbose_name_plural="Путевые листы"