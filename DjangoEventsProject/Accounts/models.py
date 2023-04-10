from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


GENDER_CHOICES = [
     ('M', 'Male'),
     ('F', 'Female'),
]
class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     address = models.CharField(max_length=30, blank=True)
     email = models.CharField(max_length=30, blank=True, unique=True)
     age=models.IntegerField()
     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M' )
     phone_no = models.CharField(max_length = 10)

         
     USERNAME_FIELD = "email"
     REQUIRED_FIELDS = ['first_name','last_name']
