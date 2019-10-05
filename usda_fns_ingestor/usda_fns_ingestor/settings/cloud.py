import os
from pathlib import Path
from .base import *  # noqa
from .env import env
from secret import generate_random_string


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get_credential('APP_SECRET_KEY', generate_random_string(50))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Get to the base directory above the current app directory.  In cloud.gov, HOME is /home/vcap/app.
# Going one level above to /home/vcap
BASE_DIR = Path(os.getenv("HOME"))
LOGS_DIR = Path(BASE_DIR).joinpath('logs')
LOGS_DIR.mkdir(exist_ok=True)

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
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGS_DIR, 'usda_fns_ingestor.log'),
            'formatter': 'verbose',
        },

        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
        'django': {
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.template': {
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': 'INFO',
        },
        'ReVAL': {
            'handlers': ['console', 'file'],
            'propagate': True,
            'level': 'INFO',
        }
    },
}
