"""
WSGI config for dentima_class project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from my_project import MyWSGIApp



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dentima_class.settings')

application = MyWSGIApp()
application = WhiteNoise(application, root= BASE_DIR / 'static')