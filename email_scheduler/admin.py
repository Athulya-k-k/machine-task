from django.contrib import admin
from .models import ScheduledEmail

@admin.register(ScheduledEmail)
class ScheduledEmailAdmin(admin.ModelAdmin):
    list_display = ('recipients', 'subject', 'scheduled_time', 'is_sent', 'created_at')
    list_filter = ('is_sent', 'scheduled_time')
    search_fields = ('recipients', 'subject', 'body')



