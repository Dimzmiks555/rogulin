from django.contrib import admin

# Register your models here.

from .models import Employee, Transport, City, Company, Trailer

# Register your models here.

admin.site.register(Transport)
admin.site.register(Employee)
admin.site.register(City)
admin.site.register(Company)
admin.site.register(Trailer)