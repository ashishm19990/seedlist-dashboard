"""Add health check endpoint for wsgi application."""
import typing

from django.core.handlers.wsgi import WSGIHandler


def health_check(application: "WSGIHandler", health_url: str) -> typing.Callable:
    """Add health check view for wsgi application."""

    def health_check_wrapper(environ: dict, start_response: typing.Callable) -> "WSGIHandler":
        if environ.get("PATH_INFO") == health_url:
            start_response("200 OK", [("Content-Type", "text/plain")])
            return []
        return application(environ, start_response)

    return health_check_wrapper
