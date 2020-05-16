from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null = True) 
    address = models.CharField(max_length=200, null = True) 
    phone = models.CharField(max_length=200, null = True) 
    email = models.CharField(max_length=200, null = True) 

    def __str__(self):
        return str(self.name)

class Tag(models.Model):
    TAG_CAT = (('Used','Used'),
                ('New','New'),
                ('Last Chanse','Last Chense'),
                )
    name = models.CharField(max_length = 200, choices = TAG_CAT)

class Product(models.Model):
    PROD_CAT = (('Indor','Indor'),
                ('Out Dor','Out Dor'),
                ('Unique','Unique'),
                )
    name = models.CharField(max_length=200, null = True) 
    description = models.CharField(max_length=200, null = True) 
    category = models.CharField(max_length=200, choices = PROD_CAT)
    tag = models.ManyToManyField(Tag)    
    
    def __str__(self):
        return str(self.name)

class Order(models.Model):
    ORDER_CAT = (('Pending','Pending'),
                ('Sent','Sent'),
                ('Returned','Returned'),
                )
    name = models.CharField(max_length=200, choices = ORDER_CAT)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null = True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null = True)