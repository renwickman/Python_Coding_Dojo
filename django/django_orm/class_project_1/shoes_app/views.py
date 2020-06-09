from django.shortcuts import render, HttpResponse, redirect
from .models import Shoe

def index(request):
    context = {
        "all_shoes": Shoe.objects.all()
    }
    return render(request, "shoes_table.html", context)

def process(request):
    Shoe.objects.create(
        brand=request.POST["brand"], 
        size=request.POST["size"], 
        style=request.POST["style"]
    )
    return redirect("/")

def delete(request, id):
    if request.method == "POST":
        shoe_to_delete = Shoe.objects.get(id=id)
        shoe_to_delete.delete()
    return redirect("/")

# Create your views here.
