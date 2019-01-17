from object_collector.models import Condition, ActionScenario
from .actionUtils import performAction
from .dataTypeConversion import fromBinary
from .operatorUtils import compare

def testTriggerScenario(datasource_id, value):
    conditions = Condition.objects.filter(data_source_id=datasource_id).order_by('scenario_id')

    conditions_count = len(conditions)
    current_scenario_conditions_with_datasource_verified = True
    for i in range(conditions_count):
        condition = conditions[i]

        if current_scenario_conditions_with_datasource_verified:
            if not validateCondition(condition, value):
                current_scenario_conditions_with_datasource_verified = False

        scenario_id = condition.scenario.id
        if i == conditions_count - 1 or scenario_id != conditions[i + 1].scenario.id:
            if current_scenario_conditions_with_datasource_verified:
                conditions_scenarios = Condition.objects.filter(scenario_id=scenario_id).exclude(
                    data_source_id=datasource_id)

                all_conditions_verified = True
                for conditionScenario in conditions_scenarios:
                    if not validateCondition(conditionScenario, value):
                        all_conditions_verified = False

                if all_conditions_verified:
                    launchAllActionScenario(scenario_id)

            current_scenario_conditions_with_datasource_verified = True


def validateCondition(condition, value):
    operator = condition.operator.name
    condition_value = fromBinary(condition.value, condition.data_source.data_type.name)

    return compare(operator, value, condition_value)


def launchAllActionScenario(scenario_id):
    actionsScenario = ActionScenario.objects.filter(scenario_id=scenario_id)

    for actionScenario in actionsScenario:
        payload = fromBinary(actionScenario.payload, actionScenario.data_type)
        performAction(actionScenario.action.id, payload)



