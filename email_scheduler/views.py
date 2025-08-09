from rest_framework import generics
from .models import ScheduledEmail
from .serializers import ScheduledEmailSerializer

class EmailScheduleCreateView(generics.CreateAPIView):
    queryset = ScheduledEmail.objects.all()
    serializer_class = ScheduledEmailSerializer

class EmailScheduleListView(generics.ListAPIView):
    queryset = ScheduledEmail.objects.all()
    serializer_class = ScheduledEmailSerializer

class EmailScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScheduledEmail.objects.all()
    serializer_class = ScheduledEmailSerializer
