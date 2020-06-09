from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    print("in the hello function")
    return "Hello World!"

@app.route("/dojo")
def hello_dojo():
    print("in the dojo function")
    return "Dojo!"

@app.route("/say/<name>")
def hi_person(name):
    print("*"*80)
    print("in hi_person function")
    print(name)
    return f"Hi {name}!"

@app.route("/repeat/<int:number>/<name>")
def hrepeat(number,name):
    print("in the repeat function")
    return number*(name+", ")

@app.errorhandler(404)
def page_not_found(e):
    # print("in the not_found function")
    return "Sorry! No response.  Try again.", 404


if __name__ == "__main__":
    app.run(debug=True)

    # return str(number) + (name+", ")   Ninja Bonus