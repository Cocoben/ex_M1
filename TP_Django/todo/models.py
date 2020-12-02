import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    created_date = models.DateTimeField('Date de creation')
    content = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    def __str__(self):
        return self.content
    def was_published_recently(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)