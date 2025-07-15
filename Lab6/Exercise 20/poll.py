from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize dictionary to store vote number
votes = {"Cats": 0, "Dogs": 0}

@app.route("/poll", methods=["GET", "POST"])
def poll():
    if request.method == "POST":
        vote = request.form["vote"]
        if vote in votes:
            votes[vote] += 1  # Update vote count for selection
        return render_template("poll.html", votes=votes, results=True)
    
    return render_template("poll.html", votes=votes, results=False)

if __name__ == "__main__":
    app.run(debug=True)
