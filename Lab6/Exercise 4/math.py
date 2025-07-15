from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/square")
def square():
    num = request.args.get("num")
    if num is None:
        return render_template("square.html")
    try:
        n = int(num)
        result = n * n
        return render_template("answer.html", num=n, square=result)
    except ValueError:
        return render_template("square.html", error="Please enter a valid number.")
    
if __name__ == "__main__":
    app.run(debug=True)