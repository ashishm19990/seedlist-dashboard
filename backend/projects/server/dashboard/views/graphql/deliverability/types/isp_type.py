"""This module provides DjangoObjectType for Isp model."""
from deliverability.models import Isp
from graphene_django.types import DjangoObjectType


class IspType(DjangoObjectType):
    """IspType ObjectType Isp, for GraphQL query response."""

    class Meta:
        """Meta information for IspType."""

        model = Isp
        fields = (
            "id",
            "name",
            "region",
            "protocol",
            "host",
            "port",
            "usessl",
            "inboxfoldername",
            "receivediplast",
            "receivedregex",
            "ipheader",
            "ipheaderregex",
            "bulkfoldername",
            "bulkheader",
            "bulkheaderregex",
            "bulksubjectlineregex",
            "spfheader",
            "spfpassregex",
            "spfvalueregex",
            "dkimheader",
            "dkimpassregex",
            "dkimvalueregex",
            "domainkeysheader",
            "domainkeyspassregex",
            "domainkeysvalueregex",
            "senderidheader",
            "senderidpassregex",
            "senderidvalueregex",
            "enabled",
            "country",
        )
