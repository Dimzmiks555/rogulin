from django.shortcuts import render

# Create your views here.
def print_waybill(request):


    return render(request, "reports/waybill_template.html", context={

    })