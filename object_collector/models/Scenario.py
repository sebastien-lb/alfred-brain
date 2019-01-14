import uuid
from django.db import models


from .Action import Action


class Scenario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=(30))
    action = models.ManyToManyField(Action)

    class Meta:
        verbose_name_plural = "Scenarios"
