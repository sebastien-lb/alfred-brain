import uuid
from django.db import models

from .SmartObject import SmartObject
from .ReferenceType import DataType

class Action(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=(30))
    command = models.CharField(max_length=(100))
    payload = models.ForeignKey(DataType, blank=True, null=True, on_delete=models.CASCADE)
    smart_object = models.ForeignKey(SmartObject, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Actions"
