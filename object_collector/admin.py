from django.contrib import admin

from .models import SmartObject


# Register your models here.
class SmartObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'address_ip', 'port')


admin.site.register(SmartObject, SmartObjectAdmin)