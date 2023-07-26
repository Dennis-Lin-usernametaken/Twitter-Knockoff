from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    body = models.TextField() # the user can write anything to create a post
    created_on = models.DateTimeField(default=timezone.now) # dates on post
    author = models.ForeignKey(User, on_delete=models.CASCADE) # delete function

# copy paste because they do the same thing
class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
