from django.shortcuts import render, HttpResponse, redirect
from . models import *
from django.contrib import messages



def showIndex(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, "display_shows.html", context)


def startShow(request):
    return render(request, "add_show.html")


def createShow(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    Show.objects.create(
        title=request.POST["title"],
        network=request.POST["network"],
        release=request.POST["release"],
        desc=request.POST["desc"]
    )
    return redirect(f'/shows')


def displayShow(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, "read_show.html", context)

def editShow(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, "edit_show.html", context)

def submitEdit(request, id):
    show = Show.objects.get(id=id)
    if request.POST["title"]:
        show.title = request.POST["title"]

    if request.POST["network"]:
        show.network = request.POST["network"]
    
    if request.POST["release"]:
        show.release = request.POST["release"]

    if request.POST["desc"]:
        show.desc = request.POST["desc"]
    show.save()
    return redirect(f'/shows/{show.id}')


def deleteShow(request, id):
        show_to_delete = Show.objects.get(id=id)
        show_to_delete.delete()
        return redirect(f'/shows')