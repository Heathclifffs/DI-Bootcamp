from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField()
    adresse = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} '

