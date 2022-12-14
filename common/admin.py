from django.contrib import admin

# Register your models here.

from .models import ExpenseType, IncomeType

# Register your models here.

admin.site.register(ExpenseType)
admin.site.register(IncomeType)