
from django.db.models import signals
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .serializers import *
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=Join_events)
def send_email_on_save(sender, instance, created, **kwargs):
    if created:
        subject = 'New object created'
        message = f'A new object with ID {instance.id} was created.'
        email_from=settings.EMAIL_HOST_USER
        recipient_list = [instance.user.email]
        send_mail(subject, message, None, recipient_list, fail_silently=False)