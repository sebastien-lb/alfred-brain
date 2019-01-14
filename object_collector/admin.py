from django.contrib import admin

from .models import *


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
    list_display = ('name', 'id', 'description', 'endpoint', 'data_type', 'data_polling_type', 'smart_object')

class DataPointAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'data_source', 'value')

class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ConditionAdmin(admin.ModelAdmin):
    list_display = ('id','value','operator','scenario','data_source')

class ScenarioAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

class OperatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(SmartObject, SmartObjectAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(DataType, DataTypeAdmin)
admin.site.register(DataPollingType, DataPollingTypeAdmin)
admin.site.register(DataSource, DataSourceAdmin)
admin.site.register(DataPoint, DataPointAdmin)
admin.site.register(CategoryType, CategoryTypeAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(Scenario, ScenarioAdmin)
admin.site.register(Operator, OperatorAdmin)
