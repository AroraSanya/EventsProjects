from .serializers import *
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import signals
from django.core.mail import send_mail

@receiver(reset_password_token_created)
def password_reset(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="reset password mail"),
        # message:
        email_plaintext_message,
        # from:
        "arorasanya352@gmail.com",
        # to:
        [reset_password_token.user.email]
    )
  