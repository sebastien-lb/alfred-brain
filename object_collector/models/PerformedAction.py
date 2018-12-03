import uuid
from django.db import models

from .Action import Action

class PerformedAction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "PerformedActions"
