"""This module provides utility functions for settings."""
import typing


def get_installed_apps(debug: bool) -> typing.List:
    """Provide list of installed apps for the application."""
    default_apps = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
    ]
    data_axle_packages = ["dashboard", "users", "deliverability"]
    third_party_apps = ["graphene_django", "graphql_auth", "django_filters"]

    installed_apps = default_apps + data_axle_packages + third_party_apps

    if debug:
        dev_dependencies = [
            "corsheaders",
        ]
        installed_apps = installed_apps + dev_dependencies

    return installed_apps


def get_middleware(debug: bool) -> typing.List:
    """Provide list of middlewares for the application."""
    middleware = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]
    middleware.insert(
        middleware.index("django.middleware.common.CommonMiddleware"),
        "corsheaders.middleware.CorsMiddleware",
    )
    return middleware
