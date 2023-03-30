"""This module provides all error enums."""

from enum import Enum


class ErrorCodeEnum(Enum):
    """Contains list of error codes."""

    UNAUTHORIZED = "401"
    INVALID_CREDS = "403"
