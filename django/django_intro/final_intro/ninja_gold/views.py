from django.shortcuts import render, redirect
import random


def index(request):
    if 'num' not in request.session:
        request.session["num"]=0
        request.session["activity"]=[]
    if 'num' in request.session:
        request.session["num"] < 50
    print(request.session['num'])
    return render(request,"index.html")


def process_money(request):
    if request.method == "POST":
        if request.POST['building'] == 'farm':
            farmNum = random.randint(10, 21)
            request.session["num"] += farmNum
            print(request.session["num"])
            request.session["activity"].append("you gained " + str(farmNum) + " gold")
        elif request.POST['building'] == 'cave':
            caveNum = random.randint(5, 10)
            request.session["num"] += caveNum
            print(request.session["num"])
            request.session["activity"].append("you gained " + str(caveNum) + " gold")
        elif request.POST['building'] == 'house':
            houseNum = random.randint(2,5)
            request.session["num"] += houseNum
            print(request.session["num"])
            request.session["activity"].append("you gained " + str(houseNum) + " gold")
        elif request.POST['building'] == 'casino':
            casinoNum = random.randint(-50,50)
            if casinoNum >= 0:
                request.session["num"] += casinoNum
                print(request.session["num"])
                request.session["activity"].append("you gained " + str(casinoNum) + " gold")
            else:
                request.session["num"] += casinoNum
                print(request.session["num"])
                request.session["activity"].append("you lost " + str(casinoNum) + " gold")
    else:
        print("Error!")
    return redirect('/')


def destroy(request):
    del request.session["activity"]
    del request.session["num"]
    return redirect('/')

#     print('form',request.POST)
    # hiddenInput = request.POST['building']


# Create your views here.
