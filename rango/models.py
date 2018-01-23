from django.db import models
from django.template.defaultfilters import slugify

MAX_CHAR_FIELD_LENGTH = 128


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
