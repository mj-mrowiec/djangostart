from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.CharField(max_length = 200, null = True, blank = True)
    fname = models.CharField(max_length = 200, null = True)
    lname = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return str(self.user)

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
        print('Profile has been created')
post_save.connect(create_profile, sender=User)


def updated_profile(sender, instance, created, **kwargs):
    if created == False:
        try:
            instance.profile.save()
            print('updated!')
        except:
            Profile.objects.create(user=instance)
            print('profile created for existing user')
post_save.connect(updated_profile, sender=User)