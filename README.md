## ALFRED BRAIN

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