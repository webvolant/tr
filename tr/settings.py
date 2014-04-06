# ~*~ coding: utf-8 ~*~
"""
Django settings for tr project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i9_$_c(u+=^2-#%27efecr=ff(*$c%z#q3ur=kmx-oa6$g%v!d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'localeurl',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haupt',
    'orderform',
    'south',
    'bootstrap3',
    'modeltranslation',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'localeurl.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tr.urls'

WSGI_APPLICATION = 'tr.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.contrib.auth.context_processors.auth',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'translate',
        'USER': 'root',
        'PASSWORD': '9c471de3',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

TEMPLATE_DIRS = (
    '/home/code/tr/templates', # Change this to your own directory.
)


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

# путь до папки media, в общем случае она пуста в начале

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

MEDIA_URL = '/media/'  # URL для медии в шаблонах


STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')  # пустая папка, сюда будет собирать статику collectstatic

STATIC_URL = '/static/'  # URL для шаблонов


STATICFILES_DIRS = (

    os.path.join(BASE_DIR, 'templates/css'),
)


# "Поисковики" статики. Первый ищет статику в STATICFILES_DIRS,

# второй в папках приложений.

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

REDACTOR_OPTIONS = {'removeStyles': True}


#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#DEFAULT_FROM_EMAIL = 'user@domain.com'
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.domain.com'
#EMAIL_HOST_USER = 'user@domain.com'
#EMAIL_HOST_PASSWORD = 'password'
#EMAIL_PORT = 587

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'volant247@googlemail.com'
EMAIL_HOST_PASSWORD = '9c471de3'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'volant247@googlemail.com'

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
"""
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'some.google.account@googlemail.com'
EMAIL_HOST_PASSWORD = 'pass'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'some.google.account@googlemail.com'
"""



LANGUAGE_CODE = 'ru-RU'

LANGUAGES = (
    ('ru', 'Russian'),
    ('de', 'Deutsch'),
    ('en', 'English'),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_TRANSLATION_REGISTRY = 'tr.translation'

# включаем систему перевода django
USE_I18N = True

# указываем, где лежат файлы перевода
LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)
