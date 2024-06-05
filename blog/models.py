from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
         return self.title

