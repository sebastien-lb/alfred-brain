from django.contrib import admin

from .models import SmartObject, Action, CategoryType, DataType, DataPollingType, DataSource


# Register your models here.
class SmartObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'address_ip', 'port')

class ActionAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'command', 'smart_object')

class DataTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DataPollingTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DataSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description', 'endpoint', 'entrypoint', 'data_type', 'data_polling_type', 'smart_object')

class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(SmartObject, SmartObjectAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(DataType, DataTypeAdmin)
admin.site.register(DataPollingType, DataPollingTypeAdmin)
admin.site.register(DataSource, DataSourceAdmin)
admin.site.register(CategoryType, CategoryTypeAdmin)