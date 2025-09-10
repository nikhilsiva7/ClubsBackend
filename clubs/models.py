from django.db import models

# Create your models here.

class Clubs(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.TextField()
    number=models.IntegerField()
    logo=models.ImageField(upload_to='images')
