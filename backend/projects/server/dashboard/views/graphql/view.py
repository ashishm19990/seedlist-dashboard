"""Customized GraphQLView module."""
import structlog as structlog
from graphene_django.views import GraphQLView as BaseGraphQLView
from graphql.error import GraphQLError

logger = structlog.get_logger(__name__)


class GraphQLView(BaseGraphQLView):
    """Customized GraphQLView."""

    @staticmethod
    def format_error(error: GraphQLError) -> dict:
        """Graphql Error customization."""
        formatted_error = super(GraphQLView, GraphQLView).format_error(error)
        formatted_error["error_code"] = ""

        try:
            formatted_error["error_code"] = error.original_error.code
        except AttributeError:
            logger.info("AttributeError exception occurred while formatting the GraphQL error")

        return formatted_error
