from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='gallery/', height_field=None, width_field=None, max_length=None)
    slug = models.SlugField(null=True)
    count = models.IntegerField(null=True, default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('gallery:gallery-detail', kwargs={'slug': self.slug})