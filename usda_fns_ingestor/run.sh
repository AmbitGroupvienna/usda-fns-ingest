#!/bin/bash
echo "------ Starting APP ------"
if [ $CF_INSTANCE_INDEX = "0" ]; then
    echo "----- Migrating Database -----"
    python manage.py migrate --noinput
    echo "----- Creating Superuser -----"
	python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('$ADMIN_USERNAME', '$ADMIN_EMAIL', '$ADMIN_PASSWORD')"
fi

python manage.py collectstatic --noinput
gunicorn -t 120 -k gevent -w 2 usda_fns_ingestor.wsgi:application
