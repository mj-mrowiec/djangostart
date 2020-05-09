from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User

#ORM object relationar mapper
class  Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    #author = models.ForeignKey(User, on_delete=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)