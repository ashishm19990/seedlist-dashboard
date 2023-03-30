"""This module provides definition for admin user mutations."""
import graphene
from dashboard.enums.error_codes import ErrorCodeEnum
from dashboard.exceptions import APIException
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from graphql_jwt.shortcuts import get_token

from ..types import UserType


class SeedsAdminLogin(graphene.Mutation):
    """Mutation to login for a seed admin user."""

    token = graphene.String(description=_("Token, required to authenticate."))
    user = graphene.Field(UserType, description=_("Inboxable user information."))

    class Arguments:
        """Acceptable arguments for SeedsAdminLogin mutation."""

        username = graphene.String(
            required=True, description=_("Username to authenticate the user.")
        )
        password = graphene.String(
            required=True, description=_("Password to authenticate the user.")
        )

    @classmethod
    def mutate(
        cls, root: graphene.ObjectType, info: graphene.ResolveInfo, username: str, password: str
    ) -> "SeedsAdminLogin":
        """Admin user login."""
        user = authenticate(username=username, password=password)

        if user is None:
            raise APIException(
                "Please enter correct username and password", code=ErrorCodeEnum.INVALID_CREDS.value
            )

        return cls(user=user, token=get_token(user))
