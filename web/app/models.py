from django.db import models
from django.utils import timezone

# Create your models here.
class feedback(models.Model):
    name= models.CharField(max_length=20)
    fname=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    email=models.EmailField()
    contact_number=models.IntegerField()
    comment=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)

class gatepass(models.Model):
    name=models.CharField(max_length=20)
    father_name=models.CharField(max_length=20)
    roll_no = models.IntegerField()
    branch = models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    contact_number = models.IntegerField()
    purpose_of_visit=models.CharField(max_length=50)
    date = models.CharField(max_length=20)
    entry_time = models.CharField(max_length=20)
    exit_time=models.CharField(max_length=20)





