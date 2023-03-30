"""A module router to determine a db to do particular db operation."""
from typing import Type

from django.db.models import Model

from .enums.databases import DatabaseEnum


class DbRouter:
    """A router to control database operations on models in for ymi and dan dbs."""

    route_db_ymi_labels = (
        "usr_users",
        "usr_roles",
        "usr_clients_edm",
    )
    route_db_dan_labels = (
        "ibx_isps",
        "ibx_seed_accounts",
    )

    def db_for_read(self, model: Model, **hints: dict) -> str:
        """Router function for all read operations."""
        return self.determine_database(model)

    def db_for_write(self, model: Model, **hints: dict) -> str:
        """Router function for all write operation."""
        return self.determine_database(model)

    def determine_database(self, model: Type[Model]) -> str:
        """Determine to use dan or default (ymi) db."""
        if model._meta.db_table in self.route_db_dan_labels:
            return DatabaseEnum.DATABASE_DAN.value

        return DatabaseEnum.DATABASE_DEFAULT.value
