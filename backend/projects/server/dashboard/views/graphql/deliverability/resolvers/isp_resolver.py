"""Module contains resolvers for ISPs."""
import graphene
from deliverability.models import Isp
from django.db.models import QuerySet


class IspResolver:
    """ISP resolvers."""

    @staticmethod
    def resolve_isps(
        parent: graphene.ObjectType, info: graphene.ResolveInfo, **data: dict
    ) -> QuerySet:
        """Resolve method for ISPs."""
        return Isp.objects.filter(**data).order_by("name")
