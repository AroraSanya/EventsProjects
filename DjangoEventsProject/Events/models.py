from django.db import models
from Accounts.models import Customuser
from django.core.validators import FileExtensionValidator

# Create your models here.
class Event(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    registration_url = models.TextField(default=None, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    address = models.CharField(max_length=255)
    logo = models.FileField(upload_to='location/', blank=False, null=True,
                            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    
class Join_events:
    event=models.ForeignKey(Customuser,on_delete=models.CASCADE)
    total_participants=models.ForeignKey(Customuser,on_delete=models.CASCADE)
    organised_on=title = models.CharField(max_length=255)
    joined_on=models.DateTimeField()

    

