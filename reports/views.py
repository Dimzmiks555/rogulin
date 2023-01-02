from django.shortcuts import render
from dictionary.models import Company
from .models import WayBill

# Create your views here.
def print_waybill(request, id):


    waybill = WayBill.objects.get(id=id)


    return render(request, "reports/waybill_template.html", context={
        "id": id,
        "waybill": waybill
    })