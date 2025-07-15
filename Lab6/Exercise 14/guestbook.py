from flask import Flask, render_template, request

app = Flask(__name__)

# List of guestbook entries (name and message)
guestbook_entries = [{"name": "John", "message": "Hello, this is a great site!"}]

@app.route("/guestbook", methods=["GET", "POST"])
def guestbook():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        if name and message:
            guestbook_entries.append({"name": name, "message": message})  # Add new entry to the list
        return render_template("guestbook.html", entries=guestbook_entries)

    return render_template("guestbook.html", entries=guestbook_entries)

if __name__ == "__main__":
    app.run(debug=True)
