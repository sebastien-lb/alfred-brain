from django.contrib import admin

from .models import SmartObject, Action


# Register your models here.
class SmartObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'address_ip', 'port')

class ActionAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'command', 'smart_object')

admin.site.register(SmartObject, SmartObjectAdmin)
admin.site.register(Action, ActionAdmin)