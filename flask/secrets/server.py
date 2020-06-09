from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/tell_secret', methods=["POST"])
def secret_told():
    print(request)
    print(request.form['secret'])
    return render_template("secret.html", secret=request.form['secret'])

if __name__ == "__main__":
    app.run(debug=True)