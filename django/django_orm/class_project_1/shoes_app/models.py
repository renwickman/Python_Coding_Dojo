from django.db import models

class Shoe(models.Model):
    brand = models.CharField(max_length=50)
    size = models.IntegerField()
    style = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
