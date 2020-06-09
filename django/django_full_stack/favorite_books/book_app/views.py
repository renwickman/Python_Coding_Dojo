from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def createUser(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            print("User's password entered was " + request.POST['password'])
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_pw, email=request.POST['email'])
            print("User's password has been changed to " + user.password)
    return redirect('/')

def addBook(request):
context = {
    "user_uploaded"=User.objects.first().books_uploaded.all()
}
return render(request, 'add_book.html', context)

# Create your views here.
