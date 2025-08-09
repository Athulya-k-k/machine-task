import os
from celery import Celery
from celery.schedules import crontab 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Load settings from Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Set timezone AFTER app is created
app.conf.timezone = 'Asia/Kolkata'

# Auto-discover tasks
app.autodiscover_tasks()

# Beat schedule
app.conf.beat_schedule = {
    'send-pending-emails-every-minute': {
        'task': 'email_scheduler.tasks.send_scheduled_emails',
        'schedule': crontab(minute='*'),  # every minute
    },
}
