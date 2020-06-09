from django.db import models
import re
from datetime import date, datetime

class UserManager(models.Manager):
    def basic_validator(self, requestPOST):
        errors = {}
        myDate = date.today()
        formattedDate = datetime.strptime(requestPOST['birthday'], '%Y-%m-%d')
        if (formattedDate.year + 13, formattedDate.month, formattedDate.day) > (int(myDate.year), int(myDate.month), int(myDate.day)):
            errors['too_young'] = "User is too young"
        EMAIL_REGEX = re.compile(r'^[A-Za-z0-9]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if (formattedDate.year, formattedDate.month, formattedDate.day) > (int(myDate.year), int(myDate.month), int(myDate.day)):
            errors['date_wrong'] = 'Please enter past date.'
        if len(requestPOST['name']) < 3:
            errors['name'] = "Name is too short"
        users_with_name = User.objects.filter(name=requestPOST['name'])
        if len(users_with_name) > 0:
            errors['duplicate'] = "Name already taken"
        if len(requestPOST['password']) < 8:
            errors['password'] = "Password is too short"
        if requestPOST['password'] != requestPOST['password_conf']:
            errors['no_match'] = "Password and Password Confirmation must match"
        if not EMAIL_REGEX.match(requestPOST['email']):
            errors["email_regex"] = "Email must be valid email"
        if not (requestPOST['name'].isalpha()):
            errors["alpha"] = "Name cannot contain numbers!"
        return errors

class User(models.Model):
    name = models.CharField(max_length=60)
    password = models.TextField()
    email = models.CharField(max_length=255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.CharField(max_length=250)
    user = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
