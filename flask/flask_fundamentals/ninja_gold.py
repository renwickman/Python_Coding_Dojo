from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "sai"

import random

@app.route("/")
def dev():
    if 'num' not in session:
        session["num"]=0
        session["activity"]=[]
    return render_template('ninja_gold.html')

@app.route('/process_money', methods=["POST"])
def process():
    print ('form',request.form)
    hiddenInput = request.form['building']
    if hiddenInput == 'farm':
        farmNum = random.randint(10, 21)
        session["num"] += farmNum
        session["activity"].append("you gained " + str(farmNum) + " gold")
    elif hiddenInput == 'cave':
        caveNum = random.randint(5, 10)
        session["num"] += caveNum
        session["activity"].append("you gained " + str(caveNum) + " gold")
    elif hiddenInput == 'house':
        houseNum = random.randint(2,5)
        session["num"] += houseNum
        session["activity"].append("you gained " + str(houseNum) + " gold")
    elif hiddenInput == 'casino':
        casinoNum = random.randint(-50,50)
        session["num"] += casinoNum
        if casinoNum >= 0:
            session["activity"].append("you gained " + str(casinoNum) + " gold")
        else:
            casinoNum *= -1
            session["activity"].append("you lost " + str(casinoNum) + " gold")

    else:
        print("Error!")
    return redirect("/")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
