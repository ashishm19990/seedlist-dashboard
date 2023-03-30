"""Appconfig for dashboard app."""
from django.apps import AppConfig


class DashboardConfig(AppConfig):
    """This class includes config for dashboard django app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "dashboard"
