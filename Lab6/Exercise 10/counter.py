from flask import Flask, render_template

app = Flask(__name__)

# Global variable to track number of hits
counter = 0

@app.route("/counter")
def count_visits():
    global counter
    counter += 1  # Increment the counter variable every time the page is accessed
    return render_template("counter.html", count=counter)

if __name__ == "__main__":
    app.run(debug=True)
