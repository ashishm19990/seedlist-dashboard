"""This module provides the base settings for the server."""
import os
import sys
from pathlib import Path

import environ

from .utils import get_installed_apps, get_middleware

env = environ.Env()
ENV_FILE_PATH = os.path.join(Path(__file__).resolve().parent.parent, ".env")
env_file = Path(ENV_FILE_PATH)
if env_file.is_file():
    environ.Env.read_env(ENV_FILE_PATH)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SERVER_APPS = os.path.join(Path(__file__).resolve().parent.parent)
sys.path.insert(0, SERVER_APPS)
SECRET_KEY = env("SERVER_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

ENV_NAME = env("ENV_NAME", default="stage")

# Application definition
INSTALLED_APPS = get_installed_apps(DEBUG)

MIDDLEWARE = get_middleware(DEBUG)

ROOT_URLCONF = "server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            # So that {{code}} will be kept after render_to_string
            "string_if_invalid": "Not Available",
        },
    },
]

WSGI_APPLICATION = "server.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DB_YMI_NAME", default="inboxable"),
        "USER": env("DB_YMI_USER", default="root"),
        "PASSWORD": env("DB_YMI_PASSWORD", default="admin@1234"),
        "HOST": env("DB_YMI_HOST", default="localhost"),
        "PORT": env("DB_YMI_PORT", default="3306"),
        "TEST": {"NAME": f'test_{env("DB_YMI_NAME", default="dashboard_dan")}'},
    },
    "dan": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DB_DAN_NAME", default="inboxable"),
        "USER": env("DB_DAN_USER", default="root"),
        "PASSWORD": env("DB_DAN_PASSWORD", default="admin@1234"),
        "HOST": env("DB_DAN_HOST", default="localhost"),
        "PORT": env("DB_DAN_PORT", default="3306"),
    },
}

DATABASE_ROUTERS = [
    "dashboard.db_router.DbRouter",
]

AUTHENTICATION_BACKENDS = [
    "users.auth.SeedlistAuthBackend",
    "graphql_auth.backends.GraphQLAuthBackend",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "users.User"

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

BUILD_SHA = os.environ.get("BUILD_SHA", default="no_build_sha_found")

CSRF_TRUSTED_ORIGINS = ["https://stage-genie.apps.data-axle.com"]
