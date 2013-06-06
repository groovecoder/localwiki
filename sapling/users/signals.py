from django.contrib.auth.models import User
from django.db.models.signals import post_save

from notification import models as notification

from models import UserProfile


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)


def send_account_created_email(sender, instance, created, **kwargs):
    if created:
        notification.send([instance.user], "account_create")
post_save.connect(send_account_created_email, sender=UserProfile)
