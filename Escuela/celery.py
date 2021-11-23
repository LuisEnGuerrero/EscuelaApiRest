import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Escuela.settings')
app = Celery('Escuela')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

"""
@app.task
def hello():
    return 'hello world'
"""
