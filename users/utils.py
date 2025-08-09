# from django.core.mail import send_mail
# import random
# import string

# def generate_otp(length=6):
#     return ''.join(random.choices(string.digits, k=length))

# def send_otp_email(email, otp):
#     subject = 'Your OTP for email verification'
#     message = f'Your OTP is: {otp}'
#     send_mail(subject, message, 'admin@example.com', [email])


from django.core.mail import send_mail
from django.conf import settings
import random
import string

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

def send_otp_email(email, otp):
    subject = 'Your OTP for email verification'
    message = f'Your OTP is: {otp}'
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,  
        [email],
        fail_silently=False
    )
