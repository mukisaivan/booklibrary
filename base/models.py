from django.db import models

# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    cover = models.ImageField()

