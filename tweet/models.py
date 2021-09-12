from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils import timezone
from twitteruser.models import MyUser


class Tweet(models.Model):
    body = models.TextField()
    post_created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(MyUser, on_delete=CASCADE, null=True, related_name='tweeted')


    def __str__(self):
        return self.body
