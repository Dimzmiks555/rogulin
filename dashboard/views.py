from django.shortcuts import render
from dictionary.models import Transport, Employee
from django.db.models import Sum

# Create your views here.

 
def index(request):

    transports = Transport.objects.filter()

    for transport in transports:
    
        summ = 0

        worksheets = transport.worksheet_set.all()

        for worksheet in worksheets:
            worksheet.expense_set.all().annotate(expenses_summ=Sum('summ'))
            print(worksheets.objects.values())



    employees = Employee.objects.all()


    return render(request, "dashboard/dashboard.html", context={
        'transports': transports,
        'employees': employees,
    })