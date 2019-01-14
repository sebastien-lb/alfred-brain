from object_collector.models import Condition, ActionScenario
from .actionUtils import performAction
from .dataTypeConversion import fromBinary


def testTriggerScenario(datasource_id, value):
    conditions = Condition.objects.filter(data_source_id=datasource_id).order_by('scenario_id')

    current_scenario_id = None
    current_scenario_conditions_with_datasource_verified = True
    for condition in conditions:
        scenario_id = condition.scenario

        if current_scenario_id != scenario_id:
            if current_scenario_id is not None and current_scenario_conditions_with_datasource_verified:
                conditionsScenarios = Condition.objects.filter(scenario_id=scenario_id).exclude(data_source_id=datasource_id)

                all_conditions_verified = True
                for conditionScenario in conditionsScenarios:
                    if not validateCondition(conditionScenario, value):
                        all_conditions_verified = False

                if all_conditions_verified:
                    launchAllActionScenario(scenario_id)

            current_scenario_id = scenario_id
            current_scenario_conditions_with_datasource_verified = True

        if current_scenario_conditions_with_datasource_verified:
            if not validateCondition(condition, value):
                current_scenario_conditions_with_datasource_verified = False


def validateCondition(condition, value):
    return True


def launchAllActionScenario(scenario_id):
    actionsScenario = ActionScenario.objects.filter(scenario_id=scenario_id)

    for actionScenario in actionsScenario:
        payload = fromBinary(actionScenario.payload)
        performAction(actionsScenario.action.id, payload)



