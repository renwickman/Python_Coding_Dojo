from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def checkerboard():
    return render_template("checkerboard.html", times=4, times_2=1)

@app.route("/<int:num>")
def checker_4(num):
    return render_template("checkerboard.html", times=num, times_2=1)


if __name__ == "__main__":
    app.run(debug=True)