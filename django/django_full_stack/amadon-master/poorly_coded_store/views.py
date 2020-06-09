from django.shortcuts import render, redirect
from .models import *

item = {'1': 4.99,
		'2': 24.99,
		'3': 49.99,
		'4': 14.99
}

def index(request):
    context = {
        "all_items": Item.objects.all()
    }
    return render(request, "store/index.html", context)

def cart(request):
    if 'total_spent' not in request.session:
        request.session['total_spent'] = 0
    if 'purchase' not in request.session:
        request.session['purchase'] = 0
    if 'item_count' not in request.session:
        request.session['item_count'] = 0
    request.session['quantity'] = request.POST['quantity']
    request.session['item_id'] = request.POST['item_id']
    request.session['purchase'] = item[request.POST['item_id']] * int(request.POST['quantity'])
    request.session['item_count'] += int(request.POST['quantity'])
    request.session['total_spent'] += float(request.session['purchase'])
    return redirect("/checkout")

def checkout(request):
    Item.objects.get(id=request.session['item_id'])
    return render(request, "store/checkout.html")

def clear(request):
    request.session.clear()
    return redirect('/')