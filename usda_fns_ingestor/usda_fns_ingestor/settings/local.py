import os
from .base import *  # noqa
from .env import env
from secret import generate_random_string


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get_credential('APP_SECRET_KEY', generate_random_string(50))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] "
                      "%(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S",
        },
        'simple': {
            'format': "%(levelname)s %(message)s",
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'propagate': True,
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
        'django.template': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
    },
}

DATABASES = {
    'default': dj_database_url.config(default='postgres://postgres:NOPASSWD@localhost/usda_fns_ingestor')
}