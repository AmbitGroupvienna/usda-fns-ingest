#!/bin/bash
echo "------ Starting APP ------"
if [ $CF_INSTANCE_INDEX = "0" ]; then
    echo "----- Migrating Database -----"
    python manage.py migrate --noinput
    echo "----- Creating Users -----"
    python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('user1', 'user1@usda.gov', '$APP_PASSWORD')"
	python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('user2', 'user1@usda.gov', '$APP_PASSWORD')"
	python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('user3', 'user1@usda.gov', '$APP_PASSWORD')"
fi

python manage.py collectstatic --noinput
gunicorn -t 120 -k gevent -w 2 usda_fns_ingestor.wsgi:application
