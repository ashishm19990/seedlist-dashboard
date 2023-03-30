"""Role model to store client's edm designer config."""
from django.db import models


class ClientEdm(models.Model):
    """ClientEdm for unmanaged 'usr_clients_edm' Inboxable ymi database table."""

    edm_user_id = models.CharField(unique=True, max_length=15)
    ips_client_id = models.IntegerField(unique=True, blank=True, null=True)
    is_deleted = models.IntegerField()
    inserted = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        """Meta information for ClientEdm."""

        managed = False
        db_table = "usr_clients_edm"
