"""This module provides definition for the `AuthMiddleware`."""
import typing

from dashboard.enums.error_codes import ErrorCodeEnum
from dashboard.exceptions import APIException
from django.contrib.auth.models import AbstractBaseUser, AnonymousUser
from django.http import HttpRequest
from graphene import ObjectType, ResolveInfo
from graphql_jwt.exceptions import JSONWebTokenError, JSONWebTokenExpired
from graphql_jwt.shortcuts import get_user_by_token
from graphql_jwt.utils import get_credentials

# mutations or queries that can be accessed without logging in (without auth token)
ALLOWED_MUTATIONS_AND_QUERIES = ("login",)


class AuthMiddleware:
    """Authentication middleware for graphql calls."""

    @staticmethod
    def resolve(
        next: typing.Callable, root: ObjectType, info: ResolveInfo, **kwargs: dict
    ) -> typing.Callable:
        """Check if a request is valid."""
        if not root:
            request = info.context
            user = get_user_from_request(request)
            request.user = user

            if user and not user.is_anonymous:
                return next(root, info, **kwargs)

            for selection in info.operation.selection_set.selections:
                selection_name = str(selection.name.value)
                action_disallowed = selection_name not in ALLOWED_MUTATIONS_AND_QUERIES

                if action_disallowed:
                    raise APIException(
                        "Invalid or expired access token", code=ErrorCodeEnum.UNAUTHORIZED.value
                    )

        return next(root, info, **kwargs)


def get_user_from_request(request: HttpRequest) -> AbstractBaseUser | None:
    """Get the user from request."""
    user = request.user
    auth_token = get_credentials(request)

    if auth_token:
        try:
            user = get_user_by_token(auth_token)

            if user.is_enabled == 0 or user.is_deleted == 1:
                user = AnonymousUser()
        except (JSONWebTokenExpired, JSONWebTokenError):
            raise APIException(
                "Invalid or expired access token", code=ErrorCodeEnum.UNAUTHORIZED.value
            )

    return user
