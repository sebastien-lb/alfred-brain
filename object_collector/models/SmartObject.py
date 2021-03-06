import uuid
from django.db import models
from django.core.validators import RegexValidator

from .ReferenceType import CategoryType

class SmartObject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=(30))
    address_ip = models.CharField(max_length=(100))
    port = models.CharField(max_length=(5), validators=[
        RegexValidator(
            regex='^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$',
            message='You must enter a valid port between 0 and 65535',
            code='port invalid'
        )
    ])
    category = models.ForeignKey(CategoryType, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name + "-id:" + str(self.id) + " ip:" + self.address_ip + ":" + self.port

    class Meta:
        verbose_name_plural = "SmartObjects"
