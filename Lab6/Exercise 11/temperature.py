from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/convert", methods=["GET", "POST"])
def convert():
    result = None
    error_message = None

    if request.method == "POST":
        try:
            temperature = float(request.form["temperature"])
            conversion_type = request.form["conversion_type"]

            if conversion_type == "C_to_F":
                result = (temperature * 9/5) + 32  # Celsius to Fahrenheit
            elif conversion_type == "F_to_C":
                result = (temperature - 32) * 5/9  # Fahrenheit to Celsius
        except ValueError:
            error_message = "Please enter a valid number for temperature."

    return render_template("temperature.html", result=result, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
