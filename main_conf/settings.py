"""
Django settings for main_conf project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-aq5p#3sdauvgsgou^mpw%z#g)=m&w47^q+76+)(d)z!@r3$*95'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
SITE_ID = 1
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'drf_spectacular',
    'coreapp',
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
        "DEFAULT_AUTHENTICATION_CLASSES":[
            'rest_framework_simplejwt.authentication.JWTAuthentication',
#BULAR REST API TOKEN UCHUN KERAK JWT TOKENT UCHUN YUQOORIDAGI KODDAN FOYDALANILADI
            "rest_framework.authentication.SessionAuthentication",
#       "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:3000",
    'http://127.0.0.1:8000',
    
]

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=15),
    "ROTATE_REFRESH_TOKENS": True,#Refresh token bilan access tokenni yangilagach refresh tokenni kunini yana yangilab days=15 da korsailganicha yashovchan qilibb qoyadi
#agar BLACKLIST_AFTER_ROTATION":True qilsak bu ishlatilgan eski tokenni qora royxatga qoshadi va boshqa foydalanib bolmaydi
#bu uchun yuqoriga      'rest_framework_simplejwt.token_blacklist',ni INSTALLED_APPS ga qooshish kerak boladi
    "BLACKLIST_AFTER_ROTATION": True,
# Agar buni true qilsak tokenni user model ni yangilab qoyadi    
    "UPDATE_LAST_LOGIN": True,
    "TOKEN_OBTAIN_SERIALIZER": "apiapp.serializers.MyTokenObtainPairSerializer",
}

SPECTACULAR_SETTINGS = {
    "TITLE" : "drf project",
    "DESCRIPTION":"This project was maked by drf",
    "VERSION": "1.0.0",
    'SERVE_INCLUDE_SCHEMA': False,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]


ROOT_URLCONF = 'main_conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

WSGI_APPLICATION = 'main_conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
