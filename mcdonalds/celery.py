import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mcdonalds.settings')

app = Celery('mcdonalds')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Printer task

# app.conf.beat_schedule = {
#     'print_every_5_seconds': {
#         'task': 'board.tasks.printer',
#         'schedule': 5,
#         'args': (5,),
#     },
# }

app.conf.beat_schedule = {
    'clear_board_every_minute': {
        'task': 'board.tasks.clear_old',
        'schedule': crontab(),
    },
}
app.autodiscover_tasks()
