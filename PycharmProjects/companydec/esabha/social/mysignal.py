from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from social.models import MyProfile


@receiver(post_save, sender=User)
def save_profile(sender,instance,created, **wk):
    if created:
        MyProfile.objects.create(user = instance, name=instance.username)