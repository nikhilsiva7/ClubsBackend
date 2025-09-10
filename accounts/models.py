from django.db import models
from events.models import Events

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    role=models.CharField(max_length=50)
    club_id=models.IntegerField(default=0)
    


class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.TextField()

class Enrollments(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE)
    class Meta():
        unique_together=['user_id','course_id']




