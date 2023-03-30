"""Appconfig for delivarability app."""
from django.apps import AppConfig


class DeliverabilityConfig(AppConfig):
    """This class includes config for delivarability django app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "deliverability"
