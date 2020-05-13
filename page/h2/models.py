from django.db import models

# Create your models here.


class Customer(models.Model):
    CUST_TYPE = (('PRIVATE','PRIVATE'),
                ('BUSINESS','BUSINESS'))
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    date_creation = models.DateTimeField(auto_now_add=True, null = True)
    customer_type = models.CharField(max_length = 200, choices = CUST_TYPE)

    def __str__(self):
        return self.name

class Product(models.Model):
    PROD_CAT = (('Domestic','Domestic'),
                ('Out Dor','Out Dor'),
                ('Distinct','Distinct')
    )
    name = models.CharField(max_length = 200, null = True)
    category = models.CharField(max_length = 200, choices = PROD_CAT)
    price = models.FloatField(null = False)
    date_add = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.name

class Order(models.Model):
    ORDER_STATUS = (('PENDING','PENDING'),
                    ('ORDERED','ORDERED'),
                    ('RETURNED','RETURNED')
                    )
    name = models.CharField(max_length = 200, null = False, choices = ORDER_STATUS)
    #product
    #Customer
    order_date = models.DateTimeField(max_length = 200, null = True, auto_now_add=True)

    def __str__(self):
        return self.name