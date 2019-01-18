import uuid
from django.db import models


class Operator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=(30))

    class Meta:
        verbose_name_plural = "Operators"
