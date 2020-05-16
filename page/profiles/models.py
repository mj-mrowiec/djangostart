from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name


def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.ocjecs.create(User = instance)
        print('profile.created!')

def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('Profile updated!')

post_save.connect(create_profile, sender = User)
post_save.connect(update_profile, sender = User)