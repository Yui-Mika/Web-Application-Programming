from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def score():
    if request.method == "POST":
        name = request.form["name"]
        physics = request.form["physics"]
        chemistry = request.form["chemistry"]
        maths = request.form["maths"]
        # pass data to result.html template
        return render_template("result.html", name=name, physics=physics, chemistry=chemistry, maths=maths)
    return render_template("scoreform.html")

if __name__ == "__main__":
    app.run(debug=True)