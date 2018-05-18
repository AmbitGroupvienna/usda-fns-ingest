python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('user1', 'user1@usda.gov', '$APP_PASSWORD')"
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('user2', 'user1@usda.gov', '$APP_PASSWORD')"
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_user('user3', 'user1@usda.gov', '$APP_PASSWORD')"
python manage.py runserver 0.0.0.0:8080
