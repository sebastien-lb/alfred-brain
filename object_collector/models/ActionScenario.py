from django.db import models

from .Action import Action
from .Scenario import Scenario
from .ReferenceType import DataType


class ActionScenario(models.Model):
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    payload = models.BinaryField()
    data_type = models.ForeignKey(DataType, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "ActionScenarios"
