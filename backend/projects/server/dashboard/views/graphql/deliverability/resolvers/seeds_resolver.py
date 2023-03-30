"""Module contains resolvers for Seeds."""
import graphene
from deliverability.models import SeedAccount
from django.db.models import QuerySet


class SeedsResolver:
    """Seeds resolvers."""

    @staticmethod
    def resolve_accounts(
        parent: graphene.ObjectType, info: graphene.ResolveInfo, **data: dict
    ) -> QuerySet:
        """Resolve method for listing Seed Accounts."""
        return SeedAccount.objects.filter(**data)
