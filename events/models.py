from django.db import models
from clubs.models import Clubs
from django.contrib.auth.models import User


# Create your models here.
class Events(models.Model):
    id=models.AutoField(primary_key=True)
    club_id=models.ForeignKey(Clubs,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='event_images')
    is_completed=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name} "

class EventRegistration(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    event=models.ForeignKey(Events,on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
    class Meta():
        unique_together=(('user_id','event_id'),)
    def __str__(self):
        return f"{self.user.username} registered for {self.event.title}"
    
