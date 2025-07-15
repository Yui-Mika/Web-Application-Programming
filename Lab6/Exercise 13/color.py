from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/color", methods=["GET", "POST"])
def color():
    color = "white"  # Default background color is white
    if request.method == "POST":
        color_input = request.form["color"].strip()  # Get user entered color
        if color_input:
            color = color_input  # If color is entered, change the background color
    return render_template("color.html", color=color)

if __name__ == "__main__":
    app.run(debug=True)
