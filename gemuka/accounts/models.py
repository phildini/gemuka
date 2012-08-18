from django.db import models
from django.contrib.auth import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=200)
    twitter = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s's profile" % self.user