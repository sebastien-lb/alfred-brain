from rest_framework import serializers

from .models import Action, ActionScenario, CategoryType, Condition, DataPoint, DataPollingType, DataSource, DataType, \
    Operator, PerformedAction, Scenario, SmartObject

# Serializers define the API representation.
class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ('name', 'command', 'payload', 'smart_object','id', 'important')


class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = ('id', 'name', 'description', 'data_type', 'endpoint', 'data_polling_type', 'smart_object')


class SmartObjectSerializer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField()
    data_sources = serializers.SerializerMethodField()

    class Meta:
        model = SmartObject
        fields = ('name','address_ip','port','id', 'category', 'actions', 'data_sources')


    def get_actions(self, obj):
        queryset = Action.objects.filter(smart_object=obj)
        return [ActionSerializer(m).data for m in queryset]

    def get_data_sources(self, obj):
        queryset = DataSource.objects.filter(smart_object=obj)
        return [DataSourceSerializer(m).data for m in queryset]


class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPoint
        fields = ('id','value','data_source','timestamp')


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ('id','value','operator','scenario','data_source')


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = ('id','name')


class ActionScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionScenario
        fields = ('action', 'scenario', 'payload')


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ('id','name', 'allowed_types')


class PerformedActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformedAction
        fields = ('id','action','timestamp')



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
