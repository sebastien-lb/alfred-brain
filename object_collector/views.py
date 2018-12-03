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
    def get(self, request, format=None):
        print(request)
        return Response({"success": True, "content": "Hello World!"})
