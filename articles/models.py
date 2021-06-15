from datetime import datetime
from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    img = models.ImageField( upload_to='media/articles/images', height_field=None, width_field=None, max_length=None)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField(null=True,)
    date = fieldName = models.DateTimeField(auto_now=False, auto_now_add=False)
    count = models.IntegerField(null=True, default=0)

