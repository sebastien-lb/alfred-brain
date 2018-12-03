from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
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

class DataSourceTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DataSourceType.objects.all()
    serializer_class = DataSourceTypeSerializer

class DataSourceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer

class RegisterSmartObject(APIView):
    def get(self, request, format=None):
        print(request)
        return Response({"success": True, "content": "Hello World!"})