from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title


