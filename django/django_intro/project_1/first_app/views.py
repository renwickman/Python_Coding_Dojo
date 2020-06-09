from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("placeholder to later display a list of blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, num):
    number = num
    return HttpResponse("placeholder to display blog number:"+" "+number)

def edit(request, num):
    number = num
    return HttpResponse("placeholder to edit blog"+" "+number)

def delete(request, num):
    number = num
    return redirect ("/")
# Create your views here.

