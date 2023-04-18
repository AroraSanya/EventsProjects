
from django.db.models import signals
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .serializers import *
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.db.models.signals import post_save


@receiver(post_save, sender=Join_events)
def send_email_on_save(sender, instance, created, **kwargs):
    if created:
        subject = 'Event Joined'
        message = f'EventJoined  {instance.id} was created.'
        html_message = render_to_string('signals.html', {'user': instance.user, 'event': instance.event})
        email_from=settings.EMAIL_HOST_USER
        recipient_list = [instance.user.email]
        send_mail(subject, message, email_from, recipient_list, html_message=html_message)