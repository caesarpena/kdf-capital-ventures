"""
Django settings for django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""


#AUTHENTICATION_BACKENDS = (
#    'social_core.backends.google.GoogleOAuth2',
#    'django.contrib.auth.backends.ModelBackend',
#)
#LOGIN_REDIRECT_URL = '/'

#GOOGLE_OAUTH2_CLIENT_ID = '470116914284-4qscr3hqdn9cigcbsoijm1vjrm62kfla.apps.googleusercontent.com'
#GOOGLE_OAUTH2_CLIENT_SECRET = 'n2ZOJIGCLCXdMWtjk5XPYBnJ'
#GOOGLE_WHITE_LISTED_DOMAINS = ['kdfcapitalventures.com']
#SOCIAL_AUTH_USER_MODEL = 'auth.User'




#from .email_info import *
#FOR GMAIL
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'cesar.raynell@gmail.com'
EMAIL_HOST_PASSWORD = 'Powermaxgp1!'
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#'''
#https://accounts.google.com/displayunlockcaptcha
#'''


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'J9kx8LMHg1ATZlFZ2ebgdSoLg9gcfggLfWibG3SHcK0ZysvhkJ'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['138.197.91.222','kdfcapitalventures.com','www.kdfcapitalventures.com',]

STATICSITEMAPS_ROOT_SITEMAP = 'django_project.sitemaps.sitemaps'

# Application definition

INSTALLED_APPS = (
    'loans.apps.LoansConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'django.contrib.sitemaps',
    

)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'django_project.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect', # <--

            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'loans',
        'USER': 'root',
        'PASSWORD': 'Powermaxgp1!',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = '/home/django/django_project/django_project/static'

STATICFILES_DIRS = ['/home/django/django_project/static']

STATIC_URL = '/static/'
