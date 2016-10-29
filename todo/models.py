from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self): 
        return self.name
