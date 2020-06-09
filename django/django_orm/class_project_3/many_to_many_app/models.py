from django.db import models
import re

class OwnerManager(models.Manager):
    def basic_validator(self, requestPOST):
        errors = {}
        if len(requestPOST['name']) < 3:
            errors["name"] = "Name is too short"
        NAME_REGEX = re.compile(r'^[a-zA-Z ]+$')
        EMAIL_REGEX = re.compile(r'^[A-Za-z0-9]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not NAME_REGEX.match(requestPOST['name']):
            errors["name_regex"] = "Names must only have letters"
        if not EMAIL_REGEX.match(requestPOST['email']):
            errors["email_regex"] = "Email must be valid email"
        owners_with_name = Owner.objects.filter(name=requestPOST["name"]) #use filter!
        if len(owners_with_name) > 0:
            errors["duplicate"] = "Name already taken"
        if len(requestPOST['age']) < 1:
            errors["age_missing"] = "Age is required"
        if requestPOST['age'] != "" and int(requestPOST['age']) < 0:
            errors["age"] = "Age must be at least 0"
        if requestPOST['email'] < 7:
            errors["email_short"] = "Email is too short"
        return errors


class Owner(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = OwnerManager()

class Chipmunk(models.Model):
    name = models.TextField()
    description = models.TextField()
    phone_no = models.TextField()
    owner = models.ForeignKey(Owner, related_name="chipmunks", on_delete=models.CASCADE)
    owners_that_voted_for = models.ManyToManyField(Owner, related_name="chipmunks_voted_for")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
