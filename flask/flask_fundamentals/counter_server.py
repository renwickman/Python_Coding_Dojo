from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "katana"

@app.route('/')
def root():
    if 'num' in session:
        session["num"] += 1
    else:
        session["num"] = 1
    return render_template("counter.html")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')


@app.route('/2')
def root_2():
    if 'num' in session:
        session["num"] += 2
    return render_template("counter.html")


if __name__ == "__main__":
    app.run(debug=True)