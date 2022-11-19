"""
ASGI config for instagram_clone project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from docker_server.django import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ohto.settings.prod')

application = get_asgi_application()
