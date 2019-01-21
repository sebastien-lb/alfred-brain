from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import SmartObject, Action, DataSource, DataType, DataPollingType, CategoryType
from .views import RegisterSmartObject
from rest_framework.test import APIRequestFactory, force_authenticate, RequestsClient
from rest_framework import status
from rest_framework.authtoken.models import Token
import httpretty, json

class TestSmartObjectCase(TestCase):
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


class TestActionCase(TestCase):
    def setUp(self):
        SmartObject.objects.create(name="device_test", address_ip="127.0.0.1", port="5000")
        device_test = SmartObject.objects.get(name="device_test")
        Action.objects.create(name="action", command="on", smart_object=device_test, important=True)

    def test_object_created(self):
        device_test = SmartObject.objects.get(name="device_test")
        action = Action.objects.get(name="action")
        self.assertEqual(action.command, "on")
        self.assertEqual(action.smart_object, device_test)


class TestDataTypeCase(TestCase):
    def test_object_created(self):
        DataType.objects.create(name="dataType_test")
        dataType = DataType.objects.get(name="dataType_test")

        self.assertEqual(dataType.name, "dataType_test")


class TestDataPollingTypeCase(TestCase):
    def test_object_created(self):
        DataPollingType.objects.create(name="dataPollingType_test")
        dataPollingType = DataPollingType.objects.get(name="dataPollingType_test")

        self.assertEqual(dataPollingType.name, "dataPollingType_test")

class TestCategoryTypeCase(TestCase):
    def test_object_created(self):
        CategoryType.objects.create(name="categoryType_test")
        categoryType = CategoryType.objects.get(name="categoryType_test")

        self.assertEqual(categoryType.name, "categoryType_test")

class TestDataSourceCase(TestCase):
    def setUp(self):
        SmartObject.objects.create(name="device_test", address_ip="127.0.0.1", port="5000")
        DataType.objects.create(name="dataType_test")
        DataPollingType.objects.create(name="dataPollingType_test")

        device = SmartObject.objects.get(name="device_test")
        dataType = DataType.objects.get(name="dataType_test")
        dataPollingType = DataPollingType.objects.get(name="dataPollingType_test")

        DataSource.objects.create(
            name="datasource_test",
            description="test of datasource object creation",
            data_type=dataType,
            endpoint="/temperature",
            data_polling_type=dataPollingType,
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

        dataPollingType = DataPollingType.objects.get(name="dataPollingType_test")
        self.assertEqual(dataSource.data_polling_type, dataPollingType)


class TestRegisterObject(TestCase):

    ip = "192.168.1.1"
    port = "800"
    name = "ObjectName"
    config_body = {
    "name": "coolObject",
    "type": "lamp",
    "actions": [
        {
            "name": "on",
            "command": "/on",
            "important": True
        },
        {
            "name": "off",
            "command": "/off",
            "important": True
        }
        ],
        "data-source": [
            {
                "name": "state",
                "description": "return the state",
                "endpoint": "/state",
                "data-type": "boolean",
                "data-polling-type": "ON_REQUEST"
            }
        ]
    }

    def setUp(self):
        # setUp user
        self.user = User.objects.create_user(username='testuser', email="test@test.test", password="12345")
        login = self.client.login(username='testuser', password='12345')

    @httpretty.activate
    def test_get_conf(self):

        # mock for object conf
        httpretty.register_uri(
            httpretty.GET,
            "http://" + self.ip + ":" + self.port + '/config',
            body=json.dumps(self.config_body)
        )

        # mock for object receiving server conf
        httpretty.register_uri(
            httpretty.POST,
            "http://" + self.ip + ":" + self.port + '/serverConfig',
        )

        # mock incoming http request
        data = {
            "address_ip": self.ip,
            "port": self.port,
            "name": self.name,
        }
        
        request_factory = APIRequestFactory()
        post_request = request_factory.post(path="registerDevice", data=data)
        force_authenticate(post_request, user=self.user)
        response = RegisterSmartObject.as_view()(post_request)
        print(response, response.data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
