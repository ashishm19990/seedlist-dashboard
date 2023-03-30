"""User model to store user information."""
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models

from .. import constants


class User(AbstractBaseUser):
    """User for unmanaged 'usr_users' Inboxable ymi database table."""

    id = models.AutoField(primary_key=True)
    client_id = models.IntegerField()
    user_id_mi = models.IntegerField(blank=True, null=True)
    user_id_di = models.IntegerField(blank=True, null=True)
    user_id_wi = models.IntegerField(blank=True, null=True)
    user_id_si = models.IntegerField(blank=True, null=True)
    user_id_ci = models.ForeignKey(
        "ClientEdm",
        models.DO_NOTHING,
        db_column="user_id_ci",
        to_field="ips_client_id",
        blank=True,
        null=True,
    )
    role = models.ForeignKey("Role", models.DO_NOTHING)
    company_id = models.IntegerField()
    email = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    last_ip = models.CharField(max_length=40, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    last_token = models.CharField(max_length=64, blank=True, null=True)
    timestamp_created = models.DateTimeField(blank=True, null=True)
    timestamp_modified = models.DateTimeField(blank=True, null=True)
    firstname = models.CharField(max_length=250, blank=True, null=True)
    lastname = models.CharField(max_length=250, blank=True, null=True)
    timezone = models.CharField(max_length=100, blank=True, null=True)
    email_alerts = models.IntegerField(blank=True, null=True)
    email_activity_alerts = models.IntegerField(blank=True, null=True)
    ent_api_key = models.TextField(blank=True, null=True)
    route = models.CharField(max_length=45, blank=True, null=True)
    is_360 = models.IntegerField()
    is_deleted = models.IntegerField(blank=True, null=True)
    is_enabled = models.IntegerField()

    USERNAME_FIELD = "id"
    EMAIL_FIELD = "email"

    objects = UserManager()

    def __str__(self) -> str:
        """Return user's email."""
        return str(self.email)

    def __repr__(self) -> str:
        """Return user's email."""
        return str(self.email)

    @property
    def is_superuser(self) -> bool:
        """Determine if a user is superuser."""
        return self.role_id == constants.USER_ROLE_ADMIN_ID

    def get_full_name(self) -> str:
        """Get full name of the user (firstname and lastname)."""
        return f"{self.firstname}  ${self.lastname}"

    def get_short_name(self) -> str:
        """Get a user's short name."""
        return self.firstname

    class Meta:
        """Meta information for User."""

        managed = False
        db_table = "usr_users"
