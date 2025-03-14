

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d_uw-rk2i3&*951apyu7ik1$kqm^15)^dfll*rt371(k*0reb)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jsonrpc_client',
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

ROOT_URLCONF = 'jsonrpc_qualix.urls'

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

WSGI_APPLICATION = 'jsonrpc_qualix.wsgi.application'


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


JSONRPC_ENDPOINT = "https://slb.medv.ru/api/v2/"

# Пути к сертификату и ключу
CLIENT_CERT = """-----BEGIN CERTIFICATE-----
MIIDNjCCAh4CAwX1szANBgkqhkiG9w0BAQsFADBpMQswCQYDVQQGEwJSVTEMMAoG
A1UECAwDVWZhMQwwCgYDVQQHDANVZmExDDAKBgNVBAoMA3NsYjEMMAoGA1UEAwwD
c2xiMSIwIAYJKoZIhvcNAQkBFhNzdXBwb3J0QHNsYi5tZWR2LnJ1MB4XDTI0MDYy
NDEyMDAxOVoXDTI1MDYyNDEyMDAxOVowVzELMAkGA1UEBhMCUlUxDzANBgNVBAgM
Bk1vc2NvdzEPMA0GA1UEBwwGTW9zY293MQ0wCwYDVQQKDARUZXN0MRcwFQYDVQQD
DA50ZXN0QHRlc3QudGVzdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
AJWdgDfGwHt4tQc7SQdZrI2y6EMn25t28xL7LFRsx0J1FjCei5+0m+PSN57VyETG
6ZAJGgKgkfgoDHCBxz5iLAw38tSpKxR4RvVlnsWgOi7i/eix75SN5mO0qZVkVcht
cWbvSsfCxyrSpjIRhk7P5p6cQczNLpsglm2yK7+1XhXTHH//OGQrm4bVWh2wInYu
d0uVPpApqnprHvHM5WgY4+8enAOqXa+wcZ2JNv/jTOE9w/dnjY5A3GjOmYB2evmu
4VafVdQgOpE+RXIoHMxnrnQRjgLVV1KaG9vn5aUOYgeaLe7rTrVttXc2OaietdEx
32cJCGlGtdEdJxfbsFXmMNcCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEACqiZoku2
YQFqQ/h56WqEZtehYuS7ia3XfhOTKN5jeTV3R2dFc7waxu6hCwNIHdi+rFUffJu/
vszrVbtQIoRZv3H0x0e8ZoMfdgws4xkAcdmQ6jA7MdPd/LBMPFmz9vN9N/i1uwPh
OTBqIuY8fXxwSolpqgAv2qHb7gPcSTLQfhGgcC9txSFJbQAae2lOBz5LrPMH4wfG
5NNQkLnJOfPT9aXKh0ebmYYlUlgGIbU2BqlhklMVyyDA8mU6gq/+0iI667efh/tA
UvwT7ElfIUFyZmQKyquHlUgl4jCRn3jC6IJjXtL7vvJ9D+iNCp6vz02iAdW/dCoT
EYJi14GirXpX0g==
-----END CERTIFICATE-----
"""
CLIENT_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCVnYA3xsB7eLUH
O0kHWayNsuhDJ9ubdvMS+yxUbMdCdRYwnouftJvj0jee1chExumQCRoCoJH4KAxw
gcc+YiwMN/LUqSsUeEb1ZZ7FoDou4v3ose+UjeZjtKmVZFXIbXFm70rHwscq0qYy
EYZOz+aenEHMzS6bIJZtsiu/tV4V0xx//zhkK5uG1VodsCJ2LndLlT6QKap6ax7x
zOVoGOPvHpwDql2vsHGdiTb/40zhPcP3Z42OQNxozpmAdnr5ruFWn1XUIDqRPkVy
KBzMZ650EY4C1VdSmhvb5+WlDmIHmi3u6061bbV3NjmonrXRMd9nCQhpRrXRHScX
27BV5jDXAgMBAAECggEANml9+IsBdMYs/DDM+e3cifofa1EDFrK3a1dKw3d+Lka7
57m5aL88FKpezRbNy2mWBuqweXUhMSGLiJ1CM4dropP0bfAKOVsW32dyS0he8K9g
DXEtAxdqSyeopyrC4e4fmIJ9bVICsinDBKGH+YC1zEhiy9NxWDyNSN7L92BEE+ZR
FNlvDDTf9oripVY494uKc3rm5XPKmWVQwBRHSom625ajNtG0od6TrVsyrRMDWzKu
7cgM3F4AtkfrYa5tbMKnotYXG3gfihT53G0lsK6cHPS9lh+ja6PrWZJU1f7HTz9e
plsCgY/ZH53qAqxxQCzb3JN2pwpk0hJpP3e7S8+hqQKBgQDSaLXmCYI3pTQK475L
V10QDtOPBEOy9F7sWDPr7g4eXM8QnJPPldZCAXsHyaqHG9pq2fXfWc+hATtq0/Ph
f2Cb7TdaUtt7Fr/mVpWyZMODWV2HJ/uLUdKHkTmWqbtV58lBToTKadTt51S0XQNC
WyWX3tISW/aOV5DJmQB/zEEvDwKBgQC2CJZqFvPzVIJeZ+67pIjfAyv2E7qd4oP6
C7kQWIEAYmV374HL5ED4CwpuIMq+xszQvCTcehCxiJMNO0Rs91UXtcPWecN/z4MB
upPhaJwvUcBFUE8bUKOAUcXwarRfCX60gln+nCjDL4ECKol6Kt31qVtrCN8ORwQa
1wAQqKHhuQKBgQCxt1N7+qgLy/OLBxUhmaa2+27hKx7rNdA/G7ivG6C9MHKMe1O1
T79qfMmnqEPqXjI7ceFkRv1B5kKDVoZ0/hthWBkap0VOT8bCDHvf84/Xj1GZ6MFj
yTZi3tyfTrk2M9Ie4Ozz8jOwxWUb+jvYfhfgkIkqjJZRX9ChFiP/zUt5LQKBgChY
HOYkciri9wXvaQTjgYZT0KF4W+r0MiXwBTMvOmAYbr63MYA79X5EDCq+T9EahHha
ypym3R5L07OiCBdSdeSMX3wgfojMOA/hBzd1FPCT4NY751x5cdNVzFXtgE5z70YY
gdOhTpN76s7NGK0f5RO2VlGRpMYoTSuZrSUECuTZAoGAW/nxI9T1uQdbQqOHANRn
0nrJF6yK5EtSpQqgDMkpQR1Rm3v6DtsnS3kxzaBInjI+TLOVwoe5LtfvCP1CIfmO
WaoxaJ6exwhzMIYRnIOKaTo+kvcrcZODAqLzsicYlJI3swrK2DE5hkM8Y0//t7nx
PjChutV5gBYfDNiR8twClXY=
-----END PRIVATE KEY-----
"""

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "jsonrpc_client.log",
            "formatter": "verbose",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": True,
        },
        "jsonrpc_client": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
