from django.db import models

from .Action import Action
from .Scenario import Scenario


class ActionScenario(models.Model):
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    payload = models.BinaryField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "ActionScenarios"
