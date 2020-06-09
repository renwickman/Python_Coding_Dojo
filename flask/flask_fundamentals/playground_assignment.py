from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def dev():
    return render_template('play_index.html', times=3, color='green')

@app.route("/play/<int:num>")
def num(num):
    return render_template('play_index.html', times=num, color='green')

@app.route("/play/<int:num>/<color>")
def color(num, color):
    return render_template('play_index.html', times=num, i=color)

if __name__ == "__main__":
    app.run(debug=True)