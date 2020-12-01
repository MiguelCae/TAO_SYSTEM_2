from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import Group, User

@receiver (post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        g1 = Group.objects.get(name='adoptantes')
        instance.groups.add(g1)