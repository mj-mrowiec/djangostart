from django.db import models

# Create your models here.


class Customer(models.Model):
    CUST_TYPE = (('PRIVATE','PRIVATE'),
                ('BUSINESS','BUSINESS'))
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    date_creation = models.DateTimeField(auto_now=True, null = True)
    customer_type = models.CharField(max_length = 200, choices = CUST_TYPE)

    def __str__(self):
        return self.name
