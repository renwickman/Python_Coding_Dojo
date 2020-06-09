from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def root():
    return "I made my first request!"

@app.route("/goodmorning")
def morning():
    return "Good morning!"

@app.route("/num/<int:number>")
def num(number):
    return str(number)

@app.route('/index')
def index():
    back_end_value = "Today is Wednesday"
    return render_template('index.html', 
    phrase="Here's my phrase", 
    front_end_name=back_end_value, 
    characters=['Lisa','Homer','Marge','Bart'])

if __name__ == "__main__":
    app.run(debug=True)


# @app.route("/")
# def hello():
#     print("in the hello function")
#     return "Hello Anthony!"

# @app.route("/<name>")
# def hello_person(name):
#     print("*"*80)
#     print("in hello_person function")
#     print(name)
#     return f"Hello {name}!"

# @app.route("/anthony")
# def hello_person():
#     return "Hello Anthony?"

# @app.route("/jonathan")
# def hello_person_2():
#     return "Hello Jonathan"

# print(__name__)