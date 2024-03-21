import os, sys
sys.path.insert(0, '/var/www//u2545487/data/www/kegrigorev.ru/dentima_class')
sys.path.insert(1, '/var/www/u2545487/data/www/kegrigorev.ru/dentima_class/venv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'dentima_class.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
