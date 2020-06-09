from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "guess"

import random

@app.route("/")
def start():
    if 'message' not in session:
        session['message'] =""
    if 'number' not in session:
        session["number"]=random.randint(1,101)
    return render_template('guessing_game.html')

@app.route("/guess", methods=["POST"])
def guess():
    guess=int(request.form['number'])
    if guess==(session['number']):
        session['message']="You Won! "+str(session["number"]) + " was the number"
    if guess > session['number']:
        session['message']="Too High"
    elif guess < session['number']:
        session['message']="Too Low"
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)