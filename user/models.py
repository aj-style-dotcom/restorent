from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userInfo(models.Model):
    user=models.OneToOneField(to=User, on_delete=models.CASCADE, primary_key=True)
    contactNo=models.IntegerField()
    address=models.TextField()
