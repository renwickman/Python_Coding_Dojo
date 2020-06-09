from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        validation_errors = {}

        owners_with_name = Show.objects.filter(title=postData["title"]) #use filter!
        myDate = datetime.now()
        formattedDate = myDate.strftime("%y-%m-%d")
        if len(owners_with_name) > 0:
            validation_errors["duplicate"] = "Name already taken"
        if len(postData['title']) == 0:
            validation_errors['title_blank'] = 'Please enter a title.'
        if len(postData['title']) < 2:
            validation_errors['title_short'] = 'Title must be at least 2 characters.'
        if len(postData['network']) == 0:
            validation_errors['title_blank'] = 'Please enter a network.'
        if len(postData['network']) < 3:
            validation_errors['title_short'] = 'Network must be at least 3 characters.'
        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            validation_errors['title_short'] = 'Description must be at least 10 characters.'
        if postData['release'] > formattedDate:
            validation_errors['date_wrong'] = 'Please enter past date.'
        return validation_errors

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release = models.DateTimeField()
    desc = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    objects = BlogManager()

# Create your models here.
