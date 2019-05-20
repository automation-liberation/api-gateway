from celery import Celery

celery = Celery(__name__, autofinalize=False)
