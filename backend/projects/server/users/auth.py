"""This module provides django authenticate backend to authenticate Inboxable users."""
import bcrypt
import structlog as structlog
from django.http import HttpRequest

from . import constants
from .models import User

logger = structlog.get_logger(__name__)


class SeedlistAuthBackend(object):
    """Custom authentication backend for Inboxable admin dashboard."""

    def authenticate(self, request: HttpRequest, username: str, password: str) -> User | None:
        """Authenticate an Inboxable admin user."""
        user: User | None = None

        try:
            admin_user = User.objects.get(
                email=username,
                is_360=0,
                is_deleted=0,
                is_enabled=1,
                role_id=constants.USER_ROLE_ADMIN_ID,
            )
            pwd_valid = bcrypt.checkpw(
                bytes(password, "utf-8"), bytes(admin_user.password, "utf-8")
            )

            if admin_user and pwd_valid:
                user = self.get_user(admin_user.id)
        except User.DoesNotExist:
            logger.info("DoesNotExist exception occurred during authenticating user")

        return user

    def get_user(self, user_id: int) -> User | None:
        """get_user mechanism for an Inboxable user."""
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
