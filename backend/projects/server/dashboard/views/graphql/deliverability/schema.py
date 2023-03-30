"""This module provides schema objects for deliverability."""
import graphene
from django.utils.translation import gettext as _

from . import mutations
from .resolvers import IspResolver, SeedsResolver
from .types import IspType, SeedAccountType


class Mutation(graphene.ObjectType):
    """Consolidated mutation which includes all 'deliverability' mutations."""

    toggle_seed_accounts = mutations.ToggleSeedAccounts.Field()


class Query(graphene.ObjectType):
    """Consolidated queries which includes all 'deliverability' queries."""

    isps = graphene.List(
        IspType,
        enabled=graphene.Argument(
            graphene.Int, description=_("include enabled or not enabled isps"), required=False
        ),
        resolver=IspResolver.resolve_isps,
    )

    seeds = graphene.List(
        SeedAccountType,
        isp_id=graphene.Argument(
            graphene.String, description=_("return seeds by ISP ID"), required=True
        ),
        enabled=graphene.Argument(
            graphene.Int, description=_("include enabled or not enabled accounts"), required=False
        ),
        resolver=SeedsResolver.resolve_accounts,
    )
