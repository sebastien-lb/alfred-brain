import uuid
from django.db import models

from .ReferenceType import DataType, DataPollingType
from .SmartObject import SmartObject

class DataSource(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=(50), default='')
    description = models.CharField(max_length=(500))

    ######
    # complete route : xxx.xxx.xxx.xxx:port/path/to/ressource
    #
    # endpoint is the smart object entrypoint
    # entrypoint is the server entry point

    endpoint = models.CharField(max_length=(200), blank=True)
    entrypoint = models.CharField(max_length=(200), blank=True)

    smart_object = models.ForeignKey(SmartObject, on_delete=models.CASCADE)

    data_polling_type = models.ForeignKey(DataPollingType, on_delete=models.CASCADE)
    data_type = models.ForeignKey(DataType, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "DataSources"
