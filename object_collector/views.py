import json

import requests
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .logic import binaryConversion, getLatestDataPointFromDataSource, getLatestDataPointsFromDataSource, testTriggerScenario, performAction
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


class ConditionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer


class OperatorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer


class ScenarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer


class ActionScenarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ActionScenario.objects.all()
    serializer_class = ActionScenarioSerializer


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

                if "payloads" in action.keys() and action["payloads"][0]["type"]:
                    try:
                        # we only deal with one parameters for now and with its type
                        action_payload_type_name = action["payloads"][0]["type"]

                        print("action_payload_type", action_payload_type_name)
                        action_payload_type = DataType.objects.get(pk=action_payload_type_name)
                        action["payload"] = action_payload_type.name
                    except (KeyError, ObjectDoesNotExist):
                        return Response("Unknown Data Type for action", status=status.HTTP_400_BAD_REQUEST)

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
                except (KeyError, ObjectDoesNotExist):
                    return Response("Unknown Data Type", status=status.HTTP_400_BAD_REQUEST)
                try:
                    # check that data_polling_type_name exists
                    data_polling_type_name = ds["data-polling-type"]
                    data_polling_type = DataPollingType.objects.get(pk=data_polling_type_name)
                except (KeyError, ObjectDoesNotExist):
                    return Response("Unknown Data Polling Type", status=status.HTTP_400_BAD_REQUEST)

                data_source["data_type"] = data_type.name
                data_source["data_polling_type"] = data_polling_type.name
                data_source_serializer = DataSourceSerializer(data=data_source)

                if data_source_serializer.is_valid():
                    data_source_created = data_source_serializer.save()
                    data_source_ids[data_source_created.name] = str(data_source_created.id)

            # send server config to the object
            url = 'http://' + data.get("address_ip") + ":" + data.get("port") + "/serverConfig"
            server_config = {"url": "127.0.0.1", "port": "8000", "id": str(smart_object.id),
                             "data-source-ids": data_source_ids}
            try:
                requests.post(url, data=json.dumps(server_config), timeout=2)
            except:
                return Response("Unable to send server config to the object", status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerformActionOnObject(APIView):
    # arg:
    # action_id: id of the action you want to execute
    def post(self, request, format=None):
        data = request.data
        try:
            action_id = data["action_id"]
        except:
            return Response("action_id param is missing", status=status.HTTP_400_BAD_REQUEST)

        payload = {"payload": data["payload"]} if "payload" in data else {}

        # execute action
        correct = performAction(action_id, payload)

        if correct:
            return Response("action performed succesfully", status=status.HTTP_200_OK)
        else:
            return Response("object is unreachable", status=status.HTTP_400_BAD_REQUEST)


class LatestPointFromDataSource(APIView):

    # parameters:
    # data_source_id: id of the data source
    def get(self, request):
        try:
            data_source_id = request.GET['data_source_id']
        except MultiValueDictKeyError:
            return Response("data_source_id param is missing", status=status.HTTP_400_BAD_REQUEST)

        ret_val = getLatestDataPointFromDataSource(data_source_id)
        return Response(ret_val, status=status.HTTP_200_OK)


class SaveDataPoint(APIView):
    permission_classes = []

    # arg:
    # data_source_id: id of the data source
    # value: value of the dataPoint
    def post(self, request, format=None):
        data = request.data
        try:
            data_source_id = data["data_source_id"]
        except KeyError:
            return Response("data_source_id param is missing", status=status.HTTP_400_BAD_REQUEST)
        try:
            value = data["value"]
        except KeyError:
            return Response("value param is missing", status=status.HTTP_400_BAD_REQUEST)

        data_source = DataSource.objects.get(pk=data_source_id)
        binary_value = binaryConversion(value, data_source.data_type.name)
        data_point = {"data_source": data_source_id}

        testTriggerScenario(data_source_id, value)

        data_point_serializer = DataPointSerializer(data=data_point)
        if data_point_serializer.is_valid():
            # binary values can not be saved with serializers
            DataPoint.objects.create(data_source=data_source, value=binary_value)
            return Response("Data Point Saved", status=status.HTTP_201_CREATED)

        return Response("Unexpected Error", status=status.HTTP_400_BAD_REQUEST)


class ObjectState(APIView):
    # return the latest data point from all data sources of an object
    # parameters:
    # smart_object_id: id of the smart_object
    def get(self, request):
        try:
            smart_object_id = request.GET['smart_object_id']
        except MultiValueDictKeyError:
            return Response("smart_object_id param is missing", status=status.HTTP_400_BAD_REQUEST)

        try:
            smart_object = SmartObject.objects.get(pk=smart_object_id)
        except ObjectDoesNotExist:
            return Response("smart object does not exist", status=status.HTTP_400_BAD_REQUEST)

        data_sources = DataSource.objects.filter(smart_object=smart_object)
        ret_val = {}
        for data_source in data_sources:
            ret_val[str(data_source.id)] = getLatestDataPointFromDataSource(data_source.id)
        return Response(ret_val, status=status.HTTP_200_OK)

class DataPointHistoryFromDataSource(APIView):

    # parameters:
    # data_source_id: id of the data source
    def get(self, request):
        try:
            data_source_id = request.GET['data_source_id']
        except MultiValueDictKeyError:
            return Response("data_source_id param is missing", status=status.HTTP_400_BAD_REQUEST)

        ret_val = getLatestDataPointsFromDataSource(data_source_id)
        return Response(ret_val, status=status.HTTP_200_OK)


class ObjectHistory(APIView):
    # return the history of the data point from all data sources of an object
    # parameters:
    # smart_object_id: id of the smart_object
    def get(self, request):
        try:
            smart_object_id = request.GET['smart_object_id']
        except MultiValueDictKeyError:
            return Response("smart_object_id param is missing", status=status.HTTP_400_BAD_REQUEST)

        try:
            smart_object = SmartObject.objects.get(pk=smart_object_id)
        except ObjectDoesNotExist:
            return Response("smart object does not exist", status=status.HTTP_400_BAD_REQUEST)

        data_sources = DataSource.objects.filter(smart_object=smart_object)
        ret_val = {}
        for data_source in data_sources:
            ret_val[str(data_source.id)] = getLatestDataPointsFromDataSource(data_source.id)
        return Response(ret_val, status=status.HTTP_200_OK)
