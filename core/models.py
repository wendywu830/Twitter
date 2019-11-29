from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
  objects = models.Manager()
  content = models.CharField(max_length=140) #limit = 140
  date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  likes = models.ManyToManyField(User, related_name='likes')


class Hashtag(models.Model):
  objects = models.Manager()
  tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE) #tweet that it was used in -- gives author & date
  content = models.CharField(max_length=139)
