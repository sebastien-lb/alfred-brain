from rest_framework import serializers
from .models import SmartObject, Action, DataType, DataSourceType, DataSource 

# Serializers define the API representation.
class SmartObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartObject
        fields = ('name','address_ip','port','id')


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ('name', 'command', 'smart_object','id')


class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataType
        fields = ('name',)


class DataSourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSourceType
        fields = ('name',)


class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = ('id', 'name', 'description', 'data_type', 'endpoint', 'data_source_type', 'smart_object')

