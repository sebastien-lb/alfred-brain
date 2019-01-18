import uuid
from django.db import models
from .Operator import Operator

class DataType(models.Model):
    name = models.CharField(primary_key=True, max_length=(50))
    operator = models.ManyToManyField(Operator)

    class Meta:
        verbose_name_plural = "DataTypes"


class DataPollingType(models.Model):
    name = models.CharField(primary_key=True, max_length=(50))

    class Meta:
        verbose_name_plural = "DataPollingTypes"

class CategoryType(models.Model):
    name = models.CharField(primary_key=True, max_length=(50))

    class Meta:
        verbose_name_plural = "CategoryTypes"
