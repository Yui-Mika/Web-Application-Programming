from flask import Flask, render_template, request


app = Flask(__name__)

# List of tasks
tasks = [
    {"task": "Study", "completed": False},
    {"task": "Exercise", "completed": False}
]

@app.route("/todo", methods=["GET", "POST"])
def todo():
    if request.method == "POST":
        new_task = request.form["task"]
        tasks.append({"task": new_task, "completed": False})
        return render_template("todolist.html", tasks=tasks)

    return render_template("todolist.html", tasks=tasks)

@app.route("/toggle/<int:task_id>", methods=["GET","POST"])
def toggle(task_id):
    task = tasks[task_id]
    task["completed"] = not task["completed"] 
    return render_template("todolist.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
