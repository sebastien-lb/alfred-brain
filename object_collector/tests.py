from django.test import TestCase
from .models import SmartObject

# Create your tests here.
class SmartObjectTestCase(TestCase):
    def setUp(self):
        SmartObject.objects.create(name="device_test", address_ip="127.0.0.1", port="5000")

    def test_object_created(self):
        device_test = SmartObject.objects.get(name="device_test")
        self.assertEqual(device_test.address_ip, "127.0.0.1")
        self.assertEqual(device_test.port, "5000")