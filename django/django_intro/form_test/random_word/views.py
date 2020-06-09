from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index_random(request):
    if 'word' not in request.session:
        request.session['word'] = ""
        return render(request,"index_random.html")
    else:
        return render(request,"index_random.html")    
    

def generate(request):
    request.session['word'] = get_random_string(length=14)
    if 'num' in request.session:
        request.session["num"] += 1
    else:
        request.session["num"] = 1
    return redirect('/random_word/')

    

def reset(request):
    del request.session["word"]
    del request.session["num"]
    return redirect('/random_word/')


# Create your views here.
