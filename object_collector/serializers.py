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


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ('id','name', 'allowed_types')



class ConditionSerializer(serializers.ModelSerializer):
    operator = OperatorSerializer()
    data_source = DataSourceSerializer()

    class Meta:
        model = Condition
        fields = ('id','value','operator','scenario','data_source')


class ScenarioSerializer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField()
    conditions = serializers.SerializerMethodField()


    class Meta:
        model = Scenario
        fields = ('id','name', 'actions', 'conditions')

    def get_actions(self, obj):
        queryset = ActionScenario.objects.filter(scenario=obj)
        return [ActionScenarioSerializer(a).data for a in queryset]
    
    def get_conditions(self, obj):
        queryset = Condition.objects.filter(scenario=obj)
        return [ConditionSerializer(c).data for c in queryset]


class ActionScenarioSerializer(serializers.ModelSerializer):
    action = ActionSerializer()
    
    class Meta:
        model = ActionScenario
        fields = ('action', 'scenario', 'payload')


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
