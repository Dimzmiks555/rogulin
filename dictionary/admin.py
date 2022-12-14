from django.contrib import admin

# Register your models here.

from .models import Employee, Transport

# Register your models here.

admin.site.register(Transport)
admin.site.register(Employee)