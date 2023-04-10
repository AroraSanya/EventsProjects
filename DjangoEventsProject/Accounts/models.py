from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customuser(AbstractUser):
     address = models.CharField(max_length=30, blank=True)
     email = models.CharField(max_length=30, blank=True, unique=True)
     date_joined = models.DateTimeField(default=timezone.now)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     age=models.IntegerField()
     phone_no = models.CharField(max_length = 10)
     USERNAME_FIELD ='email' # make the user log in with the email
     REQUIRED_FIELDS = ['username','f_name','l_name']     