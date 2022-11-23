from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    info = models.TextField()
    slug = models.SlugField(unique=True)
    preview = models.ImageField(default='image.jpeg', blank=True)
    views = models.IntegerField(default=1)
    likes = models.ManyToManyField(User, related_name='likes')
    date_added = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title[:20]

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.body[:5]}"
