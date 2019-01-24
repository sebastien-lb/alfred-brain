import requests
import json

from object_collector.models import Action
from object_collector.serializers import PerformedActionSerializer


def performAction(action_id, payload):
    # execute action
    action = Action.objects.get(pk=action_id)
    url = 'http://' + action.smart_object.address_ip + ":" + action.smart_object.port + action.command
    # to be used with ESP32, we must add 'Content-Length' header
    # we also have to send an escaped dump of the payload
    dumped_payload = json.dumps(payload)
    headers = {
        'Content-Length': str(len(dumped_payload)),
        'Content-Type': "application/json"
    }
    try:
        r = requests.post(url, headers=headers, data=dumped_payload)
        print("Response : " + r.text)
    except requests.exceptions.RequestException as e:
        print(e)
        return False

    # save ActionPerformed in db
    data_performed_action = {"action": action.id}
    performed_action_serializer = PerformedActionSerializer(data=data_performed_action)
    # should always be valid, just checking for django
    if performed_action_serializer.is_valid():
        performed_action_serializer.save()

    return True
