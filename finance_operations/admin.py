from django.contrib import admin

from .models import Expense, Income, WorkSheet, ExpenseType, IncomeType

# Register your models here.

admin.site.register(Income)


@admin.register(ExpenseType)
class ExpenseTypeAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False



@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display=['__str__', 'type', 'summ', 'date']

@admin.register(IncomeType)
class IncomeTypeAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

class WorkSheetAdminInline(admin.TabularInline):
    model = Expense



@admin.register(WorkSheet)
class WorkSheetAdmin(admin.ModelAdmin):

    list_display = ['__str__']
    inlines = (WorkSheetAdminInline, )


