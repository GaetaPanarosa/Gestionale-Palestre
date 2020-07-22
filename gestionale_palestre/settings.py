import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '=!x%sd9_d@i&cr=(+e1(s7d+e*a&(%kwrfrapc@i$1jk2bfbiz'

DEBUG = True

ALLOWED_HOSTS = []

SILENCED_SYSTEM_CHECKS = ["models.E005", "fields.E304"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mathfilters',
    'core.apps.CoreConfig',
    'website.apps.WebsiteConfig',
    'course.apps.CourseConfig',
    'trainer.apps.TrainerConfig',
    'control_panel.apps.ControlPanelConfig',
    'prenotation.apps.PrenotationConfig'
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

ROOT_URLCONF = 'gestionale_palestre.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'gestionale_palestre.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gestionale_palestre',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PORT': '',
        'PASSWORD': 'root',
        'AUTOCOMMIT': True
    },
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

AUTH_USER_MODEL = 'core.CustomUser'

LANGUAGE_CODE = 'it'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

LOGIN_REDIRECT_URL_ADMIN = '/control_panel/'

LOGIN_REDIRECT_URL_UTENTE = '/profilo/'

LOGOUT_REDIRECT_URL_ADMIN = '/'

LOGOUT_REDIRECT_URL_UTENTE = '/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGOUT_REDIRECT_URL = '/'

LOGIN_URL = '/'

LOGOUT_URL = '/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
# STATIC_ROOT = os.path.join(BASE_DIR, "static/")

DATETIME_INPUT_FORMATS = ['%Y-%m-%d %H:%M:%S']

CORS_ORIGIN_ALLOW_ALL = True

SESSION_COOKIE_AGE = 36000

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
