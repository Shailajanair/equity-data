import os

import django
from celery import Celery

# set the default Django settings module for the 'celery' program.
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'equity_data.settings')

django.setup()

my_project_celery_object = Celery('equity_data', include=['historicdata.private.crons'])
my_project_celery_object.config_from_object('django.conf:settings', namespace='CELERY')

my_project_celery_object.autodiscover_tasks(lambda: settings.INSTALLED_APPS, force=True)

# my_project_celery_object.conf.broker_url = 'redis://localhost:6379/0'
my_project_celery_object.conf.broker_transport_options = {'visibility_timeout': 3600}
# my_project_celery_object.conf.result_backend = 'redis://localhost:6379/0'
