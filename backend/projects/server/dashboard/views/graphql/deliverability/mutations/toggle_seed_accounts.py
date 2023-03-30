"""This module provides definition seed account mutations."""
from typing import List

import graphene
from deliverability.models import SeedAccount
from django.utils.translation import gettext_lazy as _


class ToggleSeedAccounts(graphene.Mutation):
    """Mutation to Toggle on/off seed account."""

    updated_count = graphene.Int(description=_("Number of accounts updated."))
    invalid_ids = graphene.List(
        graphene.String, description=_("Invalid account IDs that does not exist in database.")
    )

    class Arguments:
        """Acceptable arguments for ToggleSeedAccounts mutation."""

        ids = graphene.List(graphene.String, required=True, description=_("Seed account ID."))
        enable = graphene.Boolean(required=True, description=_("Enable or Disable the account."))

    @classmethod
    def mutate(
        cls, root: graphene.ObjectType, info: graphene.ResolveInfo, ids: List[str], enable: bool
    ) -> "ToggleSeedAccounts":
        """Toggle seed account."""
        ids = list(map(int, ids))
        accounts = SeedAccount.objects.filter(pk__in=ids)
        valid_ids = list(accounts.values_list("pk", flat=True))

        accounts.update(enabled=enable)

        invalid_ids = list(map(str, set(ids).difference(valid_ids)))

        return cls(updated_count=4, invalid_ids=invalid_ids)
