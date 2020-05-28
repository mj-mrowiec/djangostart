from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Customer(models.Model):
    MY_VALUES = (('a','a'),
                ('b','b'),
                ('c','c'),)

    name = models.CharField(max_length = 200)
    clasification = models.CharField(max_length=200, choices = MY_VALUES)
    
    def __str__(self):
        return str(self.name)

class Profile(models.Model):
    name = models.CharField(max_length = 200)

@receiver(post_save, sender = User)
def new_profile(sender, instance, created, **kwargs):
    if created:
        Profile.object.create(user = instance)

def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()

post_save.connect(new_profile, sender=User)