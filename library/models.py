from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    synopsis = models.TextField()
    category = models.ManyToManyField(Category)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

