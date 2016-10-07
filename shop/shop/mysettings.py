from os.path import join
from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': join(BASE_DIR, 'shop', 'my.cnf'),
        }
    },
}
