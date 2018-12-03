import uuid
from django.db import models

from .DataSource import DataSource

class DataPoint(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.BinaryField()
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "DataPoints"
