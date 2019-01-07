import uuid
from django.db import models

from .DataSource import DataSource
from .Operator import Operator
from .Scenario import Scenario

class Condition(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.BinaryField()
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Conditions"
