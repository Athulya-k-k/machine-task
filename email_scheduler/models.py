from django.db import models
from django.utils import timezone

class ScheduledEmail(models.Model):
    recipients = models.JSONField()
 
    subject = models.CharField(max_length=255)
    body = models.TextField()
    scheduled_time = models.DateTimeField()
    is_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"To: {self.recipient} | Subject: {self.subject}"
