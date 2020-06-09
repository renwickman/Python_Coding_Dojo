from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.db.models import Count

def index(request):
    return render(request, "index.html")

def createUser(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            print("User's password entered was " + request.POST['password'])
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(name=request.POST['name'], password=hashed_pw)
            print("User's password has been changed to " + user.password)
    return redirect('/')

def login(request):
    if request.method == "POST":
        users_with_name = User.objects.filter(name=request.POST['name'])
        if users_with_name:
            user = users_with_name[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                request.session['user'] = user.name
                return redirect('/homepage')
            else:
                print("Password didn't match")
                messages.error(request, "Incorrect name or password")
        else:
            print("Name not found")
            messages.error(request, "Incorrect name or password")
    return redirect('/')

def homepage(request):
    context = {
        "all_cats": Cat.objects.annotate(votes=Count('users_who_voted_for')).order_by('-votes'),
        "user": User.objects.get(id=request.session['user_id'])
    }
    if "user_id" in request.session:
        return render(request, "main_page.html", context)
    else:
        return redirect('/') #<--- And inside of here!

def createCat(request):
    if request.method == "POST":
        errors = Cat.objects.cat_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            Cat.objects.create(
            name=request.POST["name"],
            user = User.objects.get(id=request.session['user_id'])
            )
    return redirect('/homepage')
    #Logic to create a Cat, you should validate!

def logout(request):
    request.session.clear()
    messages.info(request, "Logged out successfully!")
    return redirect('/')

def deleteCat(request, id):
    if request.method == "POST":
        cat_with_id = Cat.objects.filter(id=id)
        if cat_with_id:
            cat = cat_with_id[0]
            user = User.objects.get(id=request.session['user_id'])
            if cat.user == user:
                cat.delete()
    return redirect('/homepage')

def voteCat(request, id):
    if request.method == "POST":
        cat_with_id = Cat.objects.filter(id=id)
        if cat_with_id:
            cat = cat_with_id[0]
            user = User.objects.get(id=request.session['user_id'])
            cat.users_who_voted_for.add(user)
            #user.cats_voted_for.add(cat)
    return redirect('/homepage')

def unvoteCat(request, id):
    if request.method == "POST":
        cat_with_id = Cat.objects.filter(id=id)
        if cat_with_id:
            cat = cat_with_id[0]
            user = User.objects.get(id=request.session['user_id'])
            cat.users_who_voted_for.remove(user)
            #user.cats_voted_for.remove(cat)
    return redirect('/homepage')

def userProfile(request):
    context = {
        "user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, "one_user.html", context)

def catProfile(request, id):
    cat_with_id = Cat.objects.filter(id=id)
    if cat_with_id:
        context = {
            "cat": Cat.objects.get(id=id)
    }
        return render(request, "one_cat.html", context)
    else:
        return redirect('/homepage')