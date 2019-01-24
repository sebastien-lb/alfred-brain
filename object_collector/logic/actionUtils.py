import requests

from object_collector.models import Action
from object_collector.serializers import PerformedActionSerializer


def performAction(action_id, payload):
    # execute action
    action = Action.objects.get(pk=action_id)
    url = 'http://' + action.smart_object.address_ip + ":" + action.smart_object.port + action.command
    try:
        r = requests.post(url, json=payload )
        print("Response : " + r.text)
    except:
        return False

    # save ActionPerformed in db
    data_performed_action = {"action": action.id}
    performed_action_serializer = PerformedActionSerializer(data=data_performed_action)
    # should always be valid, just checking for django
    if performed_action_serializer.is_valid():
        performed_action_serializer.save()

    return True
