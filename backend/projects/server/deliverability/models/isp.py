"""Isp model to store ISPs."""
from django.db import models
from django.utils.translation import gettext_lazy as _


class Isp(models.Model):
    """Isp for unmanaged 'ibx_isps' Inboxable dan database table."""

    id = models.AutoField(
        primary_key=True,
        help_text=_("ISP ID."),
    )
    name = models.CharField(
        max_length=45,
        help_text=_("ISP Name."),
    )
    region = models.CharField(
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Region of the ISP."),
    )
    protocol = models.CharField(
        max_length=4,
        blank=True,
        null=True,
        help_text=_("Email protocol ISP used by ISP."),
    )
    host = models.CharField(
        max_length=31,
        blank=True,
        null=True,
        help_text=_("Email server host."),
    )
    port = models.IntegerField(
        blank=True,
        null=True,
        help_text=_("Email server port number."),
    )
    usessl = models.IntegerField(
        db_column="useSSL",
        blank=True,
        null=True,
        help_text=_("Does the server use ssl?."),
    )
    inboxfoldername = models.CharField(
        db_column="inboxFolderName",
        max_length=12,
        db_collation="utf8mb4_unicode_ci",
        blank=True,
        null=True,
        help_text=_("Name for the 'Inbox' folder for the ISP."),
    )
    receivediplast = models.IntegerField(
        db_column="receivedIpLast",
        blank=True,
        null=True,
        help_text=_("Does it contain IP in the 'Received' header."),
    )
    receivedregex = models.CharField(
        db_column="receivedRegex",
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Regex to find the 'Received' header."),
    )
    ipheader = models.CharField(
        db_column="ipHeader",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Header name to match IP."),
    )
    ipheaderregex = models.CharField(
        db_column="ipHeaderRegex",
        max_length=255,
        blank=True,
        null=True,
        help_text=_("Regex to match IP in Header."),
    )
    bulkfoldername = models.CharField(
        db_column="bulkFolderName",
        max_length=45,
        db_collation="utf8mb4_unicode_ci",
        blank=True,
        null=True,
        help_text=_("Name for the 'Bulk' folder for the ISP."),
    )
    bulkheader = models.CharField(
        db_column="bulkHeader",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Header name for the 'bulk' folder."),
    )
    bulkheaderregex = models.CharField(
        db_column="bulkHeaderRegex",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Regex to match 'bulk' headers."),
    )
    bulksubjectlineregex = models.CharField(
        db_column="bulkSubjectLineRegex",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Regex to find 'subject line'."),
    )
    maxpullrate = models.IntegerField(
        db_column="maxPullRate",
        blank=True,
        null=True,
        help_text=_("Max pull rate at a time."),
    )
    spfheader = models.CharField(
        db_column="spfHeader",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Header name to find spf record."),
    )
    spfpassregex = models.CharField(
        db_column="spfPassRegex",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Regex for spf 'pass' name."),
    )
    spfvalueregex = models.CharField(
        db_column="spfValueRegex",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Regex for spf 'pass' value."),
    )
    dkimheader = models.CharField(
        db_column="dkimHeader",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Header name to find dkim."),
    )
    dkimpassregex = models.CharField(
        db_column="dkimPassRegex",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Regex for 'dkim' pass name."),
    )
    dkimvalueregex = models.CharField(
        db_column="dkimValueRegex",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Regex for 'dkim' pass value."),
    )
    domainkeysheader = models.CharField(
        db_column="domainKeysHeader",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Name to find header's domain key."),
    )
    domainkeyspassregex = models.CharField(
        db_column="domainKeysPassRegex",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Regex to find domain key pass name."),
    )
    domainkeysvalueregex = models.CharField(
        db_column="domainKeysValueRegex",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Regex to find domain key pass value."),
    )
    senderidheader = models.CharField(
        db_column="senderIDHeader",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Header name to find 'senderid'."),
    )
    senderidpassregex = models.CharField(
        db_column="senderIDPassRegex",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Regex to find 'senderid' name."),
    )
    senderidvalueregex = models.CharField(
        db_column="senderIDValueRegex",
        max_length=45,
        blank=True,
        null=True,
        help_text=_("Regex to find 'senderid' value."),
    )
    enabled = models.IntegerField(
        blank=True,
        null=True,
        help_text=_("Is ISP enabled?."),
    )
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Country of the ISP."),
    )

    def __str__(self) -> str:
        """Return ISP name."""
        return str(self.name)

    class Meta:
        """Meta information for Isp."""

        managed = False
        db_table = "ibx_isps"
