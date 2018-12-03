from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import SmartObject, Action, DataSource, DataType, DataSourceType


# Create your tests here.
class SmartObjectTestCase(TestCase):
    def setUp(self):
        SmartObject.objects.create(name="device_test", address_ip="127.0.0.1", port="5000")

    def test_object_created(self):
        device_test = SmartObject.objects.get(name="device_test")
        self.assertEqual(device_test.address_ip, "127.0.0.1")
        self.assertEqual(device_test.port, "5000")

    def test_address_ip(self):
        smart_object = SmartObject(name="device", address_ip="abc", port="4000")
        self.assertRaises(ValidationError, smart_object.full_clean)

    def test_port(self):
        smart_object = SmartObject(name="device", address_ip="127.0.0.1", port="a")
        self.assertRaises(ValidationError, smart_object.full_clean)


class ActionTestCase(TestCase):
    def setUp(self):
        SmartObject.objects.create(name="device_test", address_ip="127.0.0.1", port="5000")
        device_test = SmartObject.objects.get(name="device_test")
        Action.objects.create(name="action", command="on", smart_object=device_test)

    def test_object_created(self):
        device_test = SmartObject.objects.get(name="device_test")
        action = Action.objects.get(name="action")
        self.assertEqual(action.command, "on")
        self.assertEqual(action.smart_object, device_test)


class DataTypeTestCase(TestCase):
    def test_object_created(self):
        DataType.objects.create(name="dataType_test")
        dataType = DataType.objects.get(name="dataType_test")

        self.assertEqual(dataType.name, "dataType_test")


class DataSourceTypeTestCase(TestCase):
    def test_object_created(self):
        DataSourceType.objects.create(name="dataSourceType_test")
        dataSourceType = DataSourceType.objects.get(name="dataSourceType_test")

        self.assertEqual(dataSourceType.name, "dataSourceType_test")


class DataSourceTestCase(TestCase):
    def setUp(self):
        SmartObject.objects.create(name="device_test", address_ip="127.0.0.1", port="5000")
        DataType.objects.create(name="dataType_test")
        DataSourceType.objects.create(name="dataSourceType_test")

        device = SmartObject.objects.get(name="device_test")
        dataType = DataType.objects.get(name="dataType_test")
        dataSourceType = DataSourceType.objects.get(name="dataSourceType_test")

        DataSource.objects.create(
            name="datasource_test",
            description="test of datasource object creation",
            data_type=dataType,
            endpoint="/temperature",
            data_source_type=dataSourceType,
            smart_object=device
        )

    def test_object_created(self):
        dataSource = DataSource.objects.get(name="datasource_test")

        self.assertEqual(dataSource.name, "datasource_test")
        self.assertEqual(dataSource.description, "test of datasource object creation")
        self.assertEqual(dataSource.endpoint, "/temperature")

        device = SmartObject.objects.get(name="device_test")
        self.assertEqual(dataSource.smart_object, device)

        dataType = DataType.objects.get(name="dataType_test")
        self.assertEqual(dataSource.data_type, dataType)

        dataSourceType = DataSourceType.objects.get(name="dataSourceType_test")
        self.assertEqual(dataSource.data_source_type, dataSourceType)
