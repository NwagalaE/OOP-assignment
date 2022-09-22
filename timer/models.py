from django.db import models

# Create your models here.

class Timer(models.Model):
    activity_time = models.DurationField()
    break_time =  models.DurationField()
    title = models.CharField(max_length=30)
    date = models.DateField()
    take_note = models.TextField(null=True)



