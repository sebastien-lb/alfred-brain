import uuid
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class SmartObject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=(30))
    address_ip = models.CharField(max_length=(15), validators=[
        RegexValidator(
            regex='^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', 
            message='You must enter a valid ip address', 
            code='ip invalid'
        )
    ])
    port = models.CharField(max_length=(5), validators=[
        RegexValidator(
            regex='^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$', 
            message='You must enter a valid port between 0 and 65535', 
            code='port invalid'
        )
    ])

    def __str__(self):
        return self.name + "-id:" + str(self.id) + " ip:" + self.address_ip + ":" + self.port

    class Meta:
        verbose_name_plural = "SmartObjects"


class Action(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=(30))
    command = models.CharField(max_length=(100))
    smart_object = models.ForeignKey(SmartObject, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Actions"


class DataType(models.Model):
    name = models.CharField(primary_key=True, max_length=(50))

    class Meta:
        verbose_name_plural = "DataTypes"


class DataSourceType(models.Model):
    name = models.CharField(primary_key=True, max_length=(50))

    class Meta:
        verbose_name_plural = "DataSourceTypes"


class DataSource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=(50), default='')
    description = models.CharField(max_length=(500))
    data_type = models.ForeignKey(DataType, on_delete=models.CASCADE)
    endpoint = models.CharField(max_length=(200))
    data_source_type = models.ForeignKey(DataSourceType, on_delete=models.CASCADE)
    smart_object = models.ForeignKey(SmartObject, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "DataSources"

