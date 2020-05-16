from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    TAG_CAT = ( ('Domestic','Domestic'),
            ('Out Door','Out Door'),
            ('Internal','Internal'),
        )
    name = models.CharField(max_length = 200, choices = TAG_CAT)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 200, null = True)
    description = models.CharField(max_length = 200, null = True)
    tag = models.ManyToManyField(Tag, null=True)
    def __str__(self):
        return self.name


class Category(models.Model):
    CAT = ( ('Domestic','Domestic'),
            ('Out Door','Out Door'),
            ('Internal','Internal'),
        )
    name = models.CharField(max_length = 200, choices = CAT)


    def __str__(self):
        return self.name


class Order(models.Model):
    ORDER_STATUS = (('Pending','Pending'),
                    ('Ordered','Ordered'),
                    ('Returned','Returned'),)
    name = models.CharField(max_length = 200, choices = ORDER_STATUS)
    product = models.ForeignKey(Product, null = True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL)

def new_profile(sender, instance, created, **kwargs):
    if created:
        Customer.object.created(user=instance)
        print('Created')

def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('Updated')



from django.db.models.signals import post_save
from django.contrib.auth.models import User

def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.models.created(User = instance)
        print('saved')
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()

