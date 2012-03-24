from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
