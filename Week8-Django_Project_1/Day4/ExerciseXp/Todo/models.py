from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15, blank=True)
    image=models.URLField()
class Todo(models.Model):
    title = models.CharField(max_length=15,blank=True)
    details = models.TextField(default='')
    date_creation= models.DateTimeField(default =  timezone.now)
    date_completion=models.DateTimeField()
    deadline_date=models.DateTimeField()
    has_been_done=models.BooleanField(default=False)
    category = models.ForeignKey(Category,   on_delete=models.CASCADE)