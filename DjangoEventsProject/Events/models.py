from django.db import models
from django.contrib.auth.models import User
from Accounts.models import Profile
from django.core.validators import FileExtensionValidator
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    address = models.CharField(max_length=255)
    event_at=models.DateTimeField(auto_now=True,null=True)
    

    @property
    def events_status(self):
        if self.end_datetime< timezone.now():
            events_status="Past events"
        elif self.start_datetime>timezone.now():
            events_status="Upcoming events"
        return events_status


    
class Join_events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    is_registered=models.BooleanField(null=True)
    has_joined=models.DateTimeField(auto_now=True)

    class Meta:
        default_related_name = 'atendees'
    def __str__(self) -> str:
        return self.user.username


    
    

    

