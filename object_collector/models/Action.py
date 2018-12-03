import uuid
from django.db import models

from .SmartObject import SmartObject

class Action(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=(30))
    command = models.CharField(max_length=(100))
    payload = models.TextField(blank=True)
    smart_object = models.ForeignKey(SmartObject, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Actions"
