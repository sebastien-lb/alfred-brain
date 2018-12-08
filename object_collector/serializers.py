from rest_framework import serializers

from .models import Action, CategoryType, DataPoint, DataPollingType, DataSource, DataType, PerformedAction, SmartObject


class SmartObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartObject
        fields = ('id', 'name', 'address_ip', 'port', 'category')


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ('name', 'command', 'payload', 'smart_object','id')


class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPoint
        fields = ('id','value','data_source','timestamp')


class PerformedActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformedAction
        fields = ('id','action','timestamp')


class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = ('id', 'name', 'description', 'data_type', 'endpoint', 'entrypoint', 'data_polling_type', 'smart_object')


# reference types

class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataType
        fields = ('name',)


class DataPollingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPollingType
        fields = ('name',)


class CategoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryType
        fields = ('name',)
