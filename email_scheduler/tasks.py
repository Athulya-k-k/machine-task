from celery import shared_task
from django.utils.timezone import now
from .models import ScheduledEmail
from django.core.mail import send_mail
from django.conf import settings
import logging
logger = logging.getLogger(__name__)


@shared_task(bind=True, max_retries=3)
def send_scheduled_emails(self):
    from django.utils.timezone import now
    due_emails = ScheduledEmail.objects.filter(scheduled_time__lte=now(), is_sent=False)
    for email in due_emails:
        try:
            send_mail(
                email.subject,
                email.body,
                settings.EMAIL_HOST_USER,
                email.recipients,
                fail_silently=False,
            )
            email.is_sent = True
            email.save()
        except Exception as e:
            logger.error(f"Error sending email to {email.recipients}: {str(e)}")
            self.retry(exc=e, countdown=60)

