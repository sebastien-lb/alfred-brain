from rest_framework import serializers
from .models import SmartObject 

# Serializers define the API representation.
class SmartObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartObject
        fields = ('name','address_ip','port')