from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=55)

class Films(models.Model):
    name = models.CharField(max_length=55)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_release = models.DateField()
    actors = models.TextField(max_length=255)
    date_show = models.DateField()
    image = models.ImageField()

