from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Gallery, self).save(*args, **kwargs)
