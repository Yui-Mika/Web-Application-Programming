from flask import Flask, render_template, request

app = Flask(__name__)

# List of events (name and date)
events = [{"name": "Webinar on Flask", "date": "2023-10-15"}]

@app.route("/events", methods=["GET", "POST"])
def events_list():
    if request.method == "POST":
        event_name = request.form["event_name"]
        event_date = request.form["event_date"]
        if event_name and event_date:
            events.append({"name": event_name, "date": event_date})  # Add new event to list
        return render_template("events.html", events=events)

    return render_template("events.html", events=events)

if __name__ == "__main__":
    app.run(debug=True)
