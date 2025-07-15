from flask import Flask, render_template, request

app = Flask(__name__)

# Task list to store tasks
tasks = [{"task": "Study", "completed": False}]

@app.route("/tasks", methods=["GET", "POST"])
def todo():
    if request.method == "POST":
        task_text = request.form["task"].strip()
        if task_text:
            tasks.append({"task": task_text, "completed": False})  # Add new task
        return render_template("tasklist.html", tasks=tasks)

    return render_template("tasklist.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
