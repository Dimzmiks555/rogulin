from django.contrib import admin
from .models import Firm, Insurance, Type

# Register your models here.



admin.site.register(Insurance)
admin.site.register(Type)
admin.site.register(Firm)