import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'Enero31499035+'

DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.auth', 
    'django.contrib.contenttypes',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'django.contrib.messages',
    'apps.recomendador',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'apps/recomendador/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'apps/recomendador/static'),
]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')