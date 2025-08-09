from django.urls import path
from .views import (
    EmailScheduleCreateView,
    EmailScheduleListView,
    EmailScheduleDetailView
)

urlpatterns = [
    path('schedule/', EmailScheduleCreateView.as_view(), name='email-schedule-create'),
    path('schedule/all/', EmailScheduleListView.as_view(), name='email-schedule-list'),
    path('schedule/<int:pk>/', EmailScheduleDetailView.as_view(), name='email-schedule-detail'),
]
