"""This file includes master graphql mutation & queries \
 inherited from dashboard modules' mutations & queries."""
import graphene

from .auth import schema as auth_schema
from .deliverability import schema as deliverability_schema


class Mutation(auth_schema.Mutation, deliverability_schema.Mutation):
    """Master graphql mutation which inherits all the dashboard app modules mutations."""

    pass


class Query(auth_schema.Query, deliverability_schema.Query):
    """Master graphql queries which inherits all the dashboard app modules queries."""

    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
