.. _usage:

Usage
=====

Using `django-site-access` is pretty simple:

1. Add the middleware to your settings::

    MIDDLEWARE_CLASSES = [
        ...
        "django.middleware.common.CommonMiddleware",
        "site_access.middleware.BasicAuthMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        ....
    ]


2. Configure the settings::

    SITE_ACCESS_SETTINGS = {
        "basic-auth": {
            "domain": "staging.yoursite.com",
            "realm": "MyStagingSite",
            "username": "someshareduser",
            "password": "somenotsosecretpassword"
        }
    }
