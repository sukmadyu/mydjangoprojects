from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField()
    slug = models.SlugField(null=True, blank=True)
    portfolio_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Portfolio, self).save(*args, **kwargs)
