"""Role model to store user's role information."""
from django.db import models


class Role(models.Model):
    """Role for unmanaged 'usr_roles' Inboxable ymi database table."""

    parent_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        """Meta information for Role."""

        managed = False
        db_table = "usr_roles"
