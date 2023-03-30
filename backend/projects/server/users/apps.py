"""Appconfig for users app."""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """This class includes config for users django app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
