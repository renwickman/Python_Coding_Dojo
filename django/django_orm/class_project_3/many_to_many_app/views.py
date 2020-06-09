from django.shortcuts import render, redirect
from .models import Owner
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def createOwner(request):
    errors = Owner.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/') #redirect back to place of form submitted to see errors
    Owner.objects.create(name=request.POST['name'], age=request.POST['age'])
    return redirect('/success')

def success(request):
    pass
# Create your views here.
