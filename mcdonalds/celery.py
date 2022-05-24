import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mcdonalds.settings')

app = Celery('mcdonalds')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'print_every_5_seconds': {
        'task': 'board.tasks.printer',
        'schedule': 5,
        'args': (5,),
    },
}

app.autodiscover_tasks()
