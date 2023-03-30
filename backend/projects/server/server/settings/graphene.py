"""This module provides the Graphene settings for the server."""
from datetime import timedelta

GRAPHENE = {
    "SCHEMA": "dashboard.schema.schema",
    "MIDDLEWARE": [
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
    ],
    "RELAY_CONNECTION_MAX_LIMIT": 100,
}

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_ALLOW_ANY_CLASSES": ["graphql_auth.mutations.ObtainJSONWebToken"],
    "JWT_EXPIRATION_DELTA": timedelta(hours=10),
}

GRAPHQL_AUTH = {
    "LOGIN_ALLOWED_FIELDS": ["email"],
    "REGISTER_MUTATION_FIELDS": ["firstname"],
    "UPDATE_MUTATION_FIELDS": ["firstname"],
    "USER_NODE_FILTER_FIELDS": {
        "email": ["exact"],
    },
}
