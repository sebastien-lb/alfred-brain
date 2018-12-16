from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

import requests
import json

from .models import *
from .serializers import *


class SmartObjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SmartObject.objects.all()
    serializer_class = SmartObjectSerializer


class ActionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class DataTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DataType.objects.all()
    serializer_class = DataTypeSerializer


class DataPollingTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DataPollingType.objects.all()
    serializer_class = DataPollingTypeSerializer


class DataSourceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer


class PerformedActionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PerformedAction.objects.all()
    serializer_class = PerformedActionSerializer


class DataPointsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer


class CategoryTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer


class RegisterSmartObject(APIView):

    def post(self, request, format=None):
        data = request.data
        serializer = SmartObjectSerializer(data=request.data)
        if serializer.is_valid():
            # try connecting the object
            url = 'http://' + data.get("address_ip") + ":" + data.get("port") + "/config"
            try:
                r = requests.get(url, timeout=2)
            except:
                return Response("Unable to connect to the object", status=status.HTTP_400_BAD_REQUEST)

            # save object
            smart_object = serializer.save()

            config = json.loads(r.text)

            for a in config["actions"]:
                action = a
                action["smart_object"] = smart_object.id
                action_serializer = ActionSerializer(data=action)

                if action_serializer.is_valid():
                    action_serializer.save()

            data_source_ids = {} 
            for ds in config["data-source"]:
                data_source = ds
                data_source["smart_object"] = smart_object.id

                try:
                    # check that data_type exists
                    data_type_name = ds["data-type"]
                    data_type = DataType.objects.get(pk=data_type_name)
                except:
                    return Response("Unknown Data Type", status=status.HTTP_400_BAD_REQUEST)

                try:
                    # check that data_polling_type_name exists
                    data_polling_type_name = ds["data-polling-type"]
                    data_polling_type = DataPollingType.objects.get(pk=data_polling_type_name)
                except:
                    return Response("Unknown Data Polling Type", status=status.HTTP_400_BAD_REQUEST)

                data_source["data_type"] = data_type.name
                data_source["data_polling_type"] = data_polling_type.name
                data_source_serializer = DataSourceSerializer(data=data_source)

                if data_source_serializer.is_valid():
                    data_source_created = data_source_serializer.save()

                    # assign entrypoint to datasource
                    entrypoint = "/entryPoint/sourceId/" + str(data_source_created.id)
                    data_source_ids[data_source_created.name] = str(data_source_created.id)
                    data_source["entrypoint"] = entrypoint
                    data_source_serializer = DataSourceSerializer(data_source_created, data=data_source)

                    if data_source_serializer.is_valid():
                        data_source_serializer.save()

            # send server config to the object
            url = 'http://' + data.get("address_ip") + ":" + data.get("port") + "/serverConfig"
            server_config = {"url": "127.0.0.1", "port": "8000", "id": str(smart_object.id), "data-source-ids": data_source_ids}
            try:
                r = requests.post(url, data=json.dumps(server_config), timeout=2)
            except:
                return Response("Unable to send server config to the object", status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerformActionOnObject(APIView):
    # arg:
    # action_id: id of the action you want to execute
    def post(self, request, format=None):
        data = request.data
        try :
            action_id = data["action_id"]
        except:
            return Response("action_id param is missing", status=status.HTTP_400_BAD_REQUEST)
        
        payload = data["payload"] if "payload" in data else {}
        
        # execute action
        action = Action.objects.get(pk=action_id)
        print(action.smart_object)
        url = 'http://' + action.smart_object.address_ip + ":" + action.smart_object.port + "/" + action.command
        try:
            r = requests.post(url, data = payload)
            print("Response : " + r.text)
        except:
            print("Response : " + r.text)
            return Response("object is unreachable", status=status.HTTP_400_BAD_REQUEST)

        # save ActionPerformed in db
        data_performed_action = {"action": action.id}
        performed_action_serializer = PerformedActionSerializer(data=data_performed_action)
        # should always be valid, just checking for django
        if performed_action_serializer.is_valid():
            performed_action_serializer.save()

        return Response("action performed succesfully", status=status.HTTP_200_OK)
        