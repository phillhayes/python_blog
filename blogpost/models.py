from __future__ import unicode_literals

from django.db import models
from categories import models as categories

# Create your models here.
class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    
    def __str__(self):
        return self.name
    

class Blogpost(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.CharField(max_length=255)
    category = models.ForeignKey(categories.Category)
    
    def __str__(self):
        return self.title