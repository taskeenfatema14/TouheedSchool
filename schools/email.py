from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User

def send_msg_via_email(email):
    subject = 'Contact Us '
    message = f'You Contacted for School'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email], fail_silently=False) # fail_silently--> control how the email sending process handles errors
    user_obj = User.objects.get(email=email)
    user_obj.save()