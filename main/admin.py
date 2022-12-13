from django.contrib import admin

from .models import Employee, Expense, ExpenseType, Income, IncomeType, Transport

# Register your models here.

admin.site.register(Transport)
admin.site.register(Employee)
admin.site.register(ExpenseType)
admin.site.register(Expense)
admin.site.register(IncomeType)
admin.site.register(Income)