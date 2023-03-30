"""This module provides schema objects for auth."""
import graphene
from graphql_auth.schema import MeQuery, UserQuery

from . import mutations


class Mutation(graphene.ObjectType):
    """Consolidated mutation which includes all auth mutations."""

    login = mutations.SeedsAdminLogin.Field()


class Query(UserQuery, MeQuery, graphene.ObjectType):
    """Consolidated queries which includes all auth queries."""

    pass
