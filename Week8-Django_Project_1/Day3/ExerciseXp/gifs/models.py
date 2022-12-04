from django.db import models
from datetime import datetime,date
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Gif(models.Model):
    title = models.CharField(max_length=100)
    URL = models.URLField()
    uploader_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default = datetime.today())
    category = models.ManyToManyField(Category, related_name='categories', blank=True)

    def __str__(self):
           return f'{self.title}'