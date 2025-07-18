# 5.1 Flask Initialization and MongoDB Connection
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["students_db"]
collection = db["students"]

# 5.2 Displaying the Student List
@app.route('/')
def index():
    students = list(collection.find())
    return render_template("index.html", students=students)


# 5.3 Adding a New Student
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        collection.insert_one({
            "name": request.form["name"],
            "age": int(request.form["age"]),
            "major": request.form["major"]
        })
        return redirect(url_for("index"))
    return render_template("form.html", student=None)


# 5.4 Editing Student Information
@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    student = collection.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        collection.update_one(
            {"_id": ObjectId(id)},
            {
                "$set": {
                    "name": request.form["name"],
                    "age": int(request.form["age"]),
                    "major": request.form["major"]
                }
            }
        )
        return redirect(url_for("index"))
    return render_template("form.html", student=student)

# 5.5 Deleting a Student
@app.route("/delete/<id>")
def delete(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
