from . import views
from django.urls import path

urlpatterns = [
    path('print_waybill/', views.print_waybill, name="print_waybill"),
]