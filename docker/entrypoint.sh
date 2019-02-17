#!/bin/sh

echo "Waiting for the mysql database"

maxcounter=45

counter=1
while ! mysql --protocol TCP -u ${DB_USER} -p ${DB_PASS} -h ${DB_HOST} --port=${DB_PORT} -e "show databases;" > /dev/null 2>&1; do
    sleep 1
    counter=`expr $counter + 1`
    if [ $counter -gt $maxcounter ]; then
        >&2 echo "We have been waiting for MySQL too long already; failing."
        exit 1
    fi;
done

echo "Connected to the database !"

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "Create SuperUser"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('${SUPER_USER_NAME}', '${SUPER_USER_EMAIL}', '${SUPER_USER_PASS}')" | python manage.py shell

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
