from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

def profile_save(sender, instance, created, **kwargs):
    if created:
        Profile.object.create(user = instance)

def profile_update(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()

post_save.connect(profile_save, sender = User)