from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Student(models.Model):
    name = models.CharField(max_length=50)
    catchphrase = models.TextField()
    teacher = models.ForeignKey(Teacher, related_name="students", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
