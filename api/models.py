from email.policy import default
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 200)
    completed = models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return self.title
