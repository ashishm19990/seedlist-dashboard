"""This module provides DjangoObjectType for SeedAccount model."""
from deliverability.models import SeedAccount
from graphene_django import DjangoObjectType


class SeedAccountType(DjangoObjectType):
    """ObjectType SeedAccountType for GraphQL query response."""

    class Meta:
        """Meta information for SeedAccountType."""

        model = SeedAccount
        fields = (
            "id",
            "isp",
            "username",
            "emailaddress",
            "enabled",
            "status",
            "priority",
            "dateadded",
            "lastleased",
            "connection_error_count",
        )
