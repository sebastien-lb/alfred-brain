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
            try :
                r = requests.get(url)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # save object
            smart_object = serializer.save()

            config = json.loads(r.text)

            for a in config["actions"]:
                action = a
                action["smart_object"] = smart_object.id
                action_serializer = ActionSerializer(data=action)

                if action_serializer.is_valid():
                    action_serializer.save()
            
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
                    data_source["entrypoint"] = entrypoint
                    data_source_serializer = DataSourceSerializer(data_source_created, data=data_source)

                    if data_source_serializer.is_valid():
                        data_source_serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
