"""This module provides DjangoObjectType for auth models."""
from graphene_django.types import DjangoObjectType
from users.models import User


class UserType(DjangoObjectType):
    """UserType ObjectType, for GraphQL query response."""

    class Meta:
        """Meta information for UserType."""

        model = User
        fields = ("id", "client_id", "email", "firstname", "lastname")
