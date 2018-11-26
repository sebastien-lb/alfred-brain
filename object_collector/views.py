from rest_framework import viewsets
from .models import SmartObject
from .serializers import SmartObjectSerializer

class SmartObjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SmartObject.objects.all()
    serializer_class = SmartObjectSerializer