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


 