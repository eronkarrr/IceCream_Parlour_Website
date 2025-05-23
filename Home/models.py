from django.db import models
import datetime

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=13)
    desc = models.TextField()
    date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.name
    
