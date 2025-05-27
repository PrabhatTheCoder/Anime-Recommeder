import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anime_recommender.settings')

app = Celery('anime_recommender')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()