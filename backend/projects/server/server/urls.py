"""server URL Configuration."""
from dashboard.views.graphql import api
from dashboard.views.graphql.view import GraphQLView
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from users.middleware import AuthMiddleware

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "graphql/",
        csrf_exempt(
            GraphQLView.as_view(schema=api.schema, graphiql=True, middleware=[AuthMiddleware()])
        ),
        name="api",
    ),  # @TODO: Remove csrf_exempt later
]
