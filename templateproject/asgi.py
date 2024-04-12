"""
ASGI config for templateproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django_ws import get_websocket_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "templateproject.settings")

application = get_websocket_application()
