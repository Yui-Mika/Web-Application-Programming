from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        if username == "admin":
            return redirect(url_for("success"))
        else:
            return render_template("loginform.html", error="Wrong username!")
    return render_template("loginform.html")
            
@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)