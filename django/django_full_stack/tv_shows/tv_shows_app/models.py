from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release = models.DateTimeField()
    desc = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    objects = BlogManager()

# Create your models here.
