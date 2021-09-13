from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils import timezone


class TwitterUser(AbstractUser):
    name = models.CharField(max_length=50)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.name