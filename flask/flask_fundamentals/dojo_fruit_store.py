from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("dojo_fruit_store.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)

    strawberry = int(request.form['strawberry'])
    raspberry = int(request.form['raspberry'])
    blackberry = int(request.form['blackberry'])
    apple = int(request.form['apple'])
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    amount = blackberry + apple + raspberry + strawberry
    student_id = request.form['student_id']
    return render_template("checkout.html", strawberry=strawberry, raspberry = raspberry, apple=apple, blackberry=blackberry, student_id=student_id, amount=amount, first_name=first_name, last_name=last_name)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)