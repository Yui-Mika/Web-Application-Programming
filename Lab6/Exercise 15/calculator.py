from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    result = None
    error_message = None

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    error_message = "Error! Division by zero."
                else:
                    result = num1 / num2
        except ValueError:
            error_message = "Invalid input! Please enter valid numbers."

    return render_template("calculator.html", result=result, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
