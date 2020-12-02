from django.db import models

# Create your models here.

class Task(models.Model):
    created_date = models.DateTimeField('Date de creation')
    content = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)