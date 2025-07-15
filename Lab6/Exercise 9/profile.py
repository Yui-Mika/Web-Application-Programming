from flask import Flask, render_template

app = Flask(__name__)

@app.route("/profile/<username>")
def profile(username):
    if username == "admin":
        return render_template("profile.html", username=username, admin=True)
    return render_template("profile.html", username=username, admin=False)

if __name__ == "__main__":
    app.run(debug=True)
