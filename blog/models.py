from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    content = models.TextField()
    content_1 = models.TextField(null=True)
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Related_to = (
        ('Technology/IT', 'Technology/IT'),
        ('Technology/Electronics', 'Technology/Electronics'),
        ('Technology/Space', 'Technology/Space'),
        ('Technology/Others', 'Technology/Others'),
        ('Technology/Apps-Softwares', 'Technology/Apps-Softwares')
    )
    type = models.CharField(max_length=25, choices=Related_to, default='Technology/Others')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):  # for redircting to the post after the creation of the same
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment1(models.Model):
    post = models.ForeignKey(Post, related_name='comments1', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.post_title, self.name)
