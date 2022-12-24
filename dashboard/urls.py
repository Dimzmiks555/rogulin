from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="dashboard"),
    path('report/', views.report, name="report"),
    path('report_expenses/', views.report_expenses, name="report_expenses"),
]