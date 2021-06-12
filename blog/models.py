from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):  #for redircting to the post after the creation of the same
        return reverse('post-detail',kwargs={'pk':self.pk})