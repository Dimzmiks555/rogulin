from django.shortcuts import render
from dictionary.models import Transport, Employee
from finance_operations.models import Expense, Income, WorkSheet
from common.models import ExpenseType
from django.db.models import Sum

# Create your views here.

 
def index(request):


    total_expenses_summ = 0
    total_incomes_summ = 0


    total_expenses = Expense.objects.filter().aggregate(expenses_summ=Sum('summ'))
    total_incomes = Income.objects.filter().aggregate(incomes_summ=Sum('summ'))
    total_expenses_summ += total_expenses['expenses_summ'] or 0
    total_incomes_summ += total_incomes['incomes_summ'] or 0

    total = {
        'expenses_summ': total_expenses_summ,
        'incomes_summ': total_incomes_summ,
        'benefit': total_incomes_summ - total_expenses_summ
    }

    print(total)


    transports = Transport.objects.filter()

    for transport in transports:
    
        expenses_summ = 0
        incomes_summ = 0

        worksheets = transport.worksheet_set.all()

        for worksheet in worksheets:
            expenses = worksheet.expense_set.all().aggregate(expenses_summ=Sum('summ'))
            incomes = worksheet.income_set.all().aggregate(incomes_summ=Sum('summ'))
            expenses_summ += expenses['expenses_summ'] or 0
            incomes_summ += incomes['incomes_summ'] or 0
        transport.expenses_summ = expenses_summ
        transport.incomes_summ = incomes_summ
        transport.benefit_summ = incomes_summ - expenses_summ


    employees = Employee.objects.all()

    for employee in employees:
    
        expenses_summ = 0
        incomes_summ = 0

        worksheets = employee.worksheet_set.all()

        for worksheet in worksheets:
            expenses = worksheet.expense_set.all().aggregate(expenses_summ=Sum('summ'))
            incomes = worksheet.income_set.all().aggregate(incomes_summ=Sum('summ'))
            expenses_summ += expenses['expenses_summ'] or 0
            incomes_summ += incomes['incomes_summ'] or 0
        employee.expenses_summ = expenses_summ
        employee.incomes_summ = incomes_summ
        employee.benefit_summ = incomes_summ - expenses_summ


    return render(request, "dashboard/dashboard.html", context={
        'transports': transports,
        'employees': employees,
        'total': total
    })

def report(request):
    transports = Transport.objects.filter()
    employees = Employee.objects.all()


    total_expenses_summ = 0
    total_incomes_summ = 0


    total_expenses = Expense.objects.filter().aggregate(expenses_summ=Sum('summ'))
    total_incomes = Income.objects.filter().aggregate(incomes_summ=Sum('summ'))
    total_expenses_summ += total_expenses['expenses_summ'] or 0
    total_incomes_summ += total_incomes['incomes_summ'] or 0

    total = {
        'expenses_summ': total_expenses_summ,
        'incomes_summ': total_incomes_summ,
        'benefit': total_incomes_summ - total_expenses_summ
    }

    print(total)


    worksheets = WorkSheet.objects.filter()

    for worksheet in worksheets:

        expenses_summ = 0
        incomes_summ = 0

        expenses = worksheet.expense_set.all().aggregate(expenses_summ=Sum('summ'))
        incomes = worksheet.income_set.all().aggregate(incomes_summ=Sum('summ'))
        expenses_summ += expenses['expenses_summ'] or 0
        incomes_summ += incomes['incomes_summ'] or 0
        worksheet.expenses_summ = expenses_summ
        worksheet.incomes_summ = incomes_summ
        worksheet.benefit_summ = incomes_summ - expenses_summ
 


    return render(request, "dashboard/report.html", context={
        'transports': transports,
        'employees': employees,
        'worksheets': worksheets,
        'total': total
    })


def report_expenses(request):
    transports = Transport.objects.filter()
    employees = Employee.objects.all()
    expense_types = ExpenseType.objects.all()


    total_expenses_summ = 0
    total_incomes_summ = 0


    total_expenses = Expense.objects.filter().aggregate(expenses_summ=Sum('summ'))
    total_incomes = Income.objects.filter().aggregate(incomes_summ=Sum('summ'))
    total_expenses_summ += total_expenses['expenses_summ'] or 0
    total_incomes_summ += total_incomes['incomes_summ'] or 0

    total = {
        'expenses_summ': total_expenses_summ,
        'incomes_summ': total_incomes_summ,
        'benefit': total_incomes_summ - total_expenses_summ
    }

    print(total)


    expenses = Expense.objects.all()

    for expense in expenses:

        expenses_summ = 0

        expense_s =  expenses.aggregate(expenses_summ=Sum('summ'))
        expenses_summ = expense_s['expenses_summ'] or 0
        expense.expenses_summ = expenses_summ
 


    return render(request, "dashboard/report_expenses.html", context={
        'transports': transports,
        'employees': employees,
        'expenses': expenses,
        'expense_types': expense_types,
        'total': total
    })