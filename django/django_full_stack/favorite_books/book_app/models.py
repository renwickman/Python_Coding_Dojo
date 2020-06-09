from django.db import models
import re
from datetime import date, datetime

class UserManager(models.Manager):
    def basic_validator(self, requestPOST):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[A-Za-z0-9]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(requestPOST['first_name']) < 2:
            errors['first_name'] = "Name is too short"
        if len(requestPOST['last_name']) < 2:
            errors['first_name'] = "Name is too short"
        name = requestPOST['first_name'] + " " + requestPOST['last_name']
        users_with_name = User.objects.filter(name=requestPOST['name'])
        if len(users_with_name) > 0:
            errors['duplicate'] = "Name already taken"
        if len(requestPOST['password']) < 8:
            errors['password'] = "Password is too short"
        if requestPOST['password'] != requestPOST['password_conf']:
            errors['no_match'] = "Password and Password Confirmation must match"
        if not EMAIL_REGEX.match(requestPOST['email']):
            errors["email_regex"] = "Email must be valid email"
        if not (requestPOST['first_name'].isalpha()):
            errors["alpha"] = "Name cannot contain numbers!"
        if not (requestPOST['last_name'].isalpha()):
            errors["alpha"] = "Name cannot contain numbers!"
        return errors

class BookManager(models.Manager):
    def book_validator(self, requestPOST):
        errors = {}
        if len(requestPOST['title']) < 0:
            errors['required'] = "Title is required"
        if len(requestPOST['desc']) < 6:
            errors['at_least'] = "Description must be at least 5 characters"
            
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded")
    users_who_like = models.ManyToManyField(User, related_name="liked_books")

# Create your models here.
