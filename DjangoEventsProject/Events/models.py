from django.db import models
from Accounts.models import Profile
from django.core.validators import FileExtensionValidator

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    registration_url = models.TextField(default=None, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    address = models.CharField(max_length=255)
    event_at=models.DateTimeField(null=True)
    
class Join_events:
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    organised_on=title = models.CharField(max_length=255)
    

    

