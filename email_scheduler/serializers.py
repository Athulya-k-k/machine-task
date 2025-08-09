# from rest_framework import serializers
# from .models import ScheduledEmail
# from django.utils import timezone
# import pytz

# class ScheduledEmailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ScheduledEmail
#         fields = '__all__'

#     def validate_scheduled_time(self, value):
#         """
#         Ensure the scheduled time is stored in UTC.
#         If the datetime is naive (no timezone), assume Asia/Kolkata.
#         """
#         if value.tzinfo is None:  # naive datetime from frontend
#             ist = pytz.timezone("Asia/Kolkata")
#             value = ist.localize(value)  # attach IST timezone

#         # Convert to UTC
#         return value.astimezone(pytz.UTC)

#     def create(self, validated_data):
#         validated_data['scheduled_time'] = self.validate_scheduled_time(
#             validated_data['scheduled_time']
#         )
#         return super().create(validated_data)

#     def update(self, instance, validated_data):
#         if 'scheduled_time' in validated_data:
#             validated_data['scheduled_time'] = self.validate_scheduled_time(
#                 validated_data['scheduled_time']
#             )
#         return super().update(instance, validated_data)



from rest_framework import serializers
from .models import ScheduledEmail
import pytz

class ScheduledEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledEmail
        fields = '__all__'

    def validate_recipients(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Recipients must be a list of emails.")
        for email in value:
            if '@' not in email:
                raise serializers.ValidationError(f"Invalid email: {email}")
        return value

    def validate_scheduled_time(self, value):
        # Store as UTC
        if value.tzinfo is None:
            ist = pytz.timezone("Asia/Kolkata")
            value = ist.localize(value)
        return value.astimezone(pytz.UTC)
