from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class Profile(models.Model):
    user = models.CharField(max_length = 20, null = True)
    first_name = models.CharField(max_length = 200, null = True)
    last_name = models.CharField(max_length = 250, null = True)

    def __str__(self):
        return str(self.name)

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.object.create(user=instance)
        print('Profile Created')

post_save.connect(create_profile, sender=User)

def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('Profile updated')

post_save.connect(update_profile, sender = USer)