from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ProfileUser(models.Model):
    user = models.ForeignKey(User, related_name='author')
    subscribers = models.ManyToManyField('self', related_name='subs', symmetrical=False)
    read_posts = models.ManyToManyField('Post', related_name='read')

    def __str__(self):
        return str(self.user)


User.profile = property(lambda u: ProfileUser.objects.get_or_create(user=u)[0])


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    entry = models.TextField()

    def __str__(self):
        return self.title
