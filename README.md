# ALFRED BRAIN

__Config Specification__

You can find an example of the `config.json` file which will be return by the object in `config.spec.json`

## Launch Alfred with Docker

```
git clone
cd alfred-docker
docker-compose up
```

To launch the stack in detached mode, then see the logs:
```
docker-compose up -d
docker-compose logs -f
```

#### Smart objects

Three objects are launched by Docker. Their ip and port are the following:

__Lamp__
```json
{
  "ip": chiros-lamp,
  "port": 9800
}
```
__Thermometer__
```json
{
  "ip": chiros-thermometer,
  "port": 9801
}
```
__RGB LED__
```json
{
  "ip": chiros-rgb-led,
  "port": 9802
}
```

## Launch alfred-brain without Docker

__Project Setup__
```
git clone
cd alfred-brain
python3 -m venv .
source ./bin/activate
pip install -r requirements.txt
```

__Database Launch__
```
cd docker
docker-compose up
```

__Apply migrations__
```
python3 manage.py migrate
```

__Start App__
```
python3 manage.py runserver
```

__Test with Postman__
```
Check that : https://stackoverflow.com/questions/50715237/how-to-test-django-rest-api-using-postman#answer-50715566
```

__Troubleshooting__

if mysqlclient not installing on MacOS, follow this :
- remove TEMPORARY mysqlclient from requirement :
- do :
```
LDFLAGS=-L/usr/local/opt/openssl/lib pip install mysqlclient 
# https://github.com/PyMySQL/mysqlclient-python/issues/13
pip install -r requirements.txt
```
## API Documentation

From Swagger : 
> https://app.swaggerhub.com/apis-docs/clement26695/Alfred/1.0.0

This documentation is the visualisation of the alfred API

