from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

def index(request):
    digits = {
        "time": strftime("%d-%m-%Y %H:%M %p", gmtime())
    }
    return render(request, 'index.html', digits)


def second(request):
    context = {
        "date": strftime("%d"),
        "month": strftime("%m"),
        "year": strftime("%Y"),
        "hour": strftime("%H"),
        "minute": strftime("%M"),
        "AM_PM": strftime("%p")
    }
    return render(request, "index_2.html", context)

# Create your views here.
