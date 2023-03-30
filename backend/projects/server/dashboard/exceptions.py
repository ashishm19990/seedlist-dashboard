"""Module for custom exceptions."""
from django.core.exceptions import PermissionDenied


class APIException(PermissionDenied):
    """Custom exception class for api errors."""

    def __init__(self, message: str, code: str | None = None):
        """Initialize error message."""
        super().__init__(message)
        self.code = code
