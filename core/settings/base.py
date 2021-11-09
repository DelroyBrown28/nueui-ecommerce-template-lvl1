import os
import environ
from pathlib import Path

env = environ.Env()
environ.Env.read_env()


DEBUG=True

BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = env('SECRET_KEY')


ALLOWED_HOSTS = ['*', 'localhost', 'http://127.0.0.1:8000/']


INSTALLED_APPS = [
    # ADMIN STUFF
    # 'jet.dashboard',
    # 'jet',
    # DJANGO STUFF
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djrichtextfield',
    'main_store',
    'basket',
    'payment',
    'account',
    'orders',
    'mptt',
    'core'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main_store.context_processors.categories',
                'basket.context_processors.basket',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Basket session id
BASKET_SESSION_ID = 'basket'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

X_FRAME_OPTIONS = 'SAMEORIGIN'

DJRICHTEXTFIELD_CONFIG = {
    'js': ['//cdn.tiny.cloud/1/ejfej7wzcg1hib8eew1onmh8d577qbpz8zcxwbb9ldzpk69m/tinymce/5/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings': {
        'menubar': False,
        'plugins': 'link image textcolor',
        'toolbar': 'bold italic | link image | removeformat | forecolor backcolor',
        'width': 700
    }
}


# Customer user model
AUTH_USER_MODEL = 'account.Customer'
LOGIN_REDIRECT_URL = '/account/dashboard'
LOGIN_URL = '/account/login/'

PASSWORD_RESET_TIMEOUT_DAYS = 2

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


STRIPE_PUBLISHABLE_KEY = 'pk_test_51HX5u6A1fnSIB3Km43MupzPhDdzE3QyyAOUnwsbTnovphUUDBuyIEDZDXo3rNw5SQHBkDuqo3keliCWShvZ3PGdN00gKgCOG4V'
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_ENDPOINT_SECRET = 'whsec_hORXdnsB5P7UFkIKg7rD8YT5ygafEc1c' 

