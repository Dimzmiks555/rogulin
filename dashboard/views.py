from django.shortcuts import render
from dictionary.models import Transport, Employee

# Create your views here.

 
def index(request):

    transports = Transport.objects.all()
    employees = Employee.objects.all()


    return render(request, "dashboard/dashboard.html", context={
        'transports': transports,
        'employees': employees,
    })