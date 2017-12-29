from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User')
    date = models.DateTimeField(default=timezone.now)
    entry = models.TextField()

    def __str__(self):
        return self.title
