"""SeedAccount model to store Seed Accounts."""
from django.db import models
from django.utils.translation import gettext_lazy as _


class SeedAccount(models.Model):
    """SeedAccount for unmanaged 'ibx_seed_accounts' Inboxable dan database table."""

    id = models.AutoField(
        primary_key=True,
        help_text=_("Seed account ID."),
    )
    isp = models.ForeignKey(
        "Isp",
        models.DO_NOTHING,
        db_column="ispID",
        help_text=_("ISP ID."),
    )
    username = models.CharField(
        max_length=255,
        help_text=_("Username of the seed."),
    )
    password = models.CharField(
        max_length=255,
        help_text=_("Password of the seed."),
    )
    dateadded = models.DateTimeField(
        db_column="dateAdded",
        blank=True,
        null=True,
        help_text=_("Timestamp added."),
    )
    lastleased = models.DateTimeField(
        db_column="lastLeased",
        blank=True,
        null=True,
        help_text=_("Last time account leased."),
    )
    lastpulled = models.DateTimeField(
        db_column="lastPulled",
        blank=True,
        null=True,
        help_text=_("Last time pulled account."),
    )
    enabled = models.IntegerField(
        blank=True,
        null=True,
        help_text=_("Is account enabled?"),
    )
    status = models.IntegerField(
        blank=True,
        null=True,
        help_text=_("Status of the seed account."),
    )
    priority = models.IntegerField(
        help_text=_("Is the seed higher priority?"),
    )
    reserved = models.IntegerField(
        help_text=_("Is the seed account reserved?"),
    )
    emailaddress = models.CharField(
        db_column="emailAddress",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Email address of the seed account."),
    )
    timestamp_update = models.DateTimeField(
        help_text=_("Last time seed account information updated timestamp."),
    )
    connection_error_count = models.IntegerField(
        help_text=_("Number of errors while processing the seed account."),
    )

    def __str__(self) -> str:
        """Return account's email."""
        return str(self.emailaddress)

    class Meta:
        """Meta information for SeedAccount."""

        managed = False
        db_table = "ibx_seed_accounts"
        unique_together = (("username", "isp"),)
