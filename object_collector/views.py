from rest_framework import viewsets
from .models import *
from .serializers import *

class SmartObjectViewSet(viewsets.ModelViewSet):
    queryset = SmartObject.objects.all()
    serializer_class = SmartObjectSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class DataTypeViewSet(viewsets.ModelViewSet):
    queryset = DataType.objects.all()
    serializer_class = DataTypeSerializer

class DataSourceTypeViewSet(viewsets.ModelViewSet):
    queryset = DataSourceType.objects.all()
    serializer_class = DataSourceTypeSerializer

class DataSourceViewSet(viewsets.ModelViewSet):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer