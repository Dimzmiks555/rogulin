from django.contrib import admin
from .models import WayBill, Ride
from django.utils.html import format_html

# Register your models here.


class WayBillAdminInline(admin.TabularInline):
    model = Ride



@admin.register(WayBill)
class WayBillAdmin(admin.ModelAdmin):

    list_display = ['__str__','print_waybill']
    inlines = (WayBillAdminInline, )

    def print_waybill(self, args):
        return format_html(f'<a href="/reports/print_waybill/{args.id}" target="_blank">Печать</a>')
     
    print_waybill.short_description = 'Печать'



admin.site.register(Ride)


