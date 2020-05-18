from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class Profiles(models.Model):
    name = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.ocjecs.created(User = instance)
        print('Profile has been created')

def updated_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.Profile.save()

post_save.connect(create_profile, sender=User)
post_save.connect(create_profile, sender=User)