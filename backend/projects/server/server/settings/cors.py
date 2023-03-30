"""This module provides the cors settings for the server."""
from corsheaders.defaults import default_headers

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "https://localhost:3000",
]
ALLOWED_HOSTS = ["*"]

CORS_ALLOW_HEADERS = list(default_headers)
