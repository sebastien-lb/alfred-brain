## ALFRED BRAIN

### Config Specification

You can find an example of the `config.json` file which will be return by the object in `config.spec.json`

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

__API Documentation__

From Swagger : 
> https://app.swaggerhub.com/apis/St00k/alfred-api/1.0.0

This documentation is the visualisation of the alfred API

__Troubleshooting__

if mysqlclient not installing on MacOS, follow this :
- remove TEMPORARY mysqlclient from requirement :
- do :
```
LDFLAGS=-L/usr/local/opt/openssl/lib pip install mysqlclient 
# https://github.com/PyMySQL/mysqlclient-python/issues/13
pip install -r requirements.txt
```