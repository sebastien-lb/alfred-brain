from rest_framework import viewsets
from .models import SmartObject
from .serializers import SmartObjectSerializer

class SmartObjectViewSet(viewsets.ModelViewSet):
    queryset = SmartObject.objects.all()
    serializer_class = SmartObjectSerializer