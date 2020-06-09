from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("dojo_survey_bonus.html")

@app.route('/result', methods=["POST"])
def secret_told():
    print(request)
    print(request.form['name'])
    print(request.form['gender'])
    print(request.form['location'])
    print(request.form['language'])
    print(request.form['text'])
    print(request.form['checkbox'])
    return render_template("survey_bonus_result.html", name=request.form["name"], gender=request.form["gender"], location=request.form["location"], language=request.form["language"], text=request.form['text'], checkbox=request.form['checkbox'])

if __name__ == "__main__":
    app.run(debug=True)