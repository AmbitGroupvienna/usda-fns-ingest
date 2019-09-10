#!/bin/bash
echo "------ Starting APP ------"
if [ $CF_INSTANCE_INDEX = "0" ]; then
    echo "----- Migrating Database -----"
    python manage.py migrate --noinput
    echo "----- Loading Initial Users -----"
	python manage.py loaddata fixtures/user.json
fi

python manage.py collectstatic --noinput
gunicorn -t 120 -k gevent -w 2 usda_fns_ingestor.wsgi:application
