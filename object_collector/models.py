import uuid
from django.db import models


# Create your models here.

class SmartObject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=(30))
    address_ip = models.CharField(max_length=(15))
    port = models.CharField(max_length=(5))

    def __str__(self):
        return self.name + "-id:" + str(self.id) + " ip:" + self.address_ip + ":" + self.port

    class Meta:
        verbose_name_plural = "SmartObjects"


 