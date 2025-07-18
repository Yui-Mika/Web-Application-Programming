from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.regex import Regex


app = Flask(__name__)

# Connect MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["students_db"] # database name
collection = db["Chapter6_students"]

# Exercise 2: add student information
@app.route("/exercise2", methods=["GET", "POST"])
def exercise2():
    if request.method == "POST":
        collection.insert_one({
            "name": request.form["name"],
            "age": int(request.form["age"]),
            "gender": request.form["gender"],
            "major": request.form["major"]
        })
        return redirect(url_for("exercise2")) 
    return render_template("Exercise2.html")

# Exercise 3: display student list
@app.route("/exercise3")
def exercise3():
    students = list(collection.find())
    return render_template("Exercise3.html", students=students)


# Exercise 4: edit student information
@app.route('/exercise4/<student_id>', methods=['GET', 'POST'])
def exercise4(student_id):
    # Optional processing: get student from MongoDB, then render form to edit or update data
    student = collection.find_one({'_id': ObjectId(student_id)})

    if request.method == 'POST':
        math = float(request.form["math"])
        literature = float(request.form["literature"])
        english = float(request.form["english"])
        gpa = round((math + literature + english) / 3, 2)

        # Exercise 12: Classify Rank
        if gpa >= 8.5:
            rank = "Excellent"
        elif gpa >= 7.0:
            rank = "Good"
        else:
            rank = "Average"


        collection.update_one(
            {"_id": ObjectId(student_id)},
            {"$set": {
                "name": request.form["name"],
                "age": int(request.form["age"]),
                "gender": request.form["gender"],
                "major": request.form["major"],
                # Exercise 10: Add subject scores
                "math": float(request.form["math"]),
                "literature": float(request.form["literature"]),
                "english": float(request.form["english"]),
                # Exercise 11: Add GPA
                "gpa": gpa,  # Update GPA
                # Exercise 12: Add rank
                "rank": rank
            }}
        )
        return redirect(url_for('exercise3'))


    return render_template('Exercise4.html', student=student)

# Exercise 5: delete student information
@app.route("/exercise5/<student_id>", methods=["POST"])
def exercise5(student_id):
    collection.delete_one({"_id": ObjectId(student_id)})
    return redirect(url_for("exercise3"))

#Exercise 6: search student information
@app.route('/exercise6', methods=['GET'])
def exercise6():
    name_query = request.args.get('name')
    students = []
    if name_query:
        students = list(collection.find({"name": name_query}))
    return render_template('Exercise6.html', students=students)

# Exercise 7: Fuzzy Search by Name
@app.route('/exercise7')
def exercise7():
    query = request.args.get('name')
    results = []

    if query:
        # Search with regular expression, case insensitive
        results = collection.find({
            "name": {
                "$regex": query,
                "$options": "i"  # Case-insensitive
            }
        })

    return render_template('Exercise7.html', students=list(results), query=query)


# Exercise 8: Filter by Major
@app.route("/exercise8", methods=["GET"])
def exercise8():
    selected_major = request.args.get("major")
    if selected_major:
        students = collection.find({"major": selected_major})
    else:
        students = []
    # Get a list of unique majors to display in the dropdown
    majors = collection.distinct("major")
    return render_template("Exercise8.html", students=students, majors=majors, selected_major=selected_major)

#Exercise 9: Count Students per Major
@app.route('/exercise9')
def exercise9():
    result = collection.aggregate([
        {
            "$group": {
                "_id": "$major",
                "count": {"$sum": 1}
            }
        }
    ])
    counts = list(result)
    return render_template('Exercise9.html', counts=counts)

# Exercise 13: Filter Excellent Students
@app.route('/exercise13')
def exercise13():
    excellent_students = list(collection.find({'gpa': {'$gte': 8}}))
    return render_template('Exercise13.html', students=excellent_students)

# Exercise 14: Find Top-Scoring Student
@app.route('/exercise14')
def exercise14():
    top_student = collection.find_one(sort=[('gpa', -1)])  # GPA decreases → take top 1
    return render_template('Exercise14.html', student=top_student)

# Êxercise 15: Filter by Age
@app.route('/exercise15', methods=['GET', 'POST'])
def exercise15():
    students = []

    if request.method == 'POST':
        try:
            min_age = int(request.form.get('min_age', 0))
            max_age = int(request.form.get('max_age', 100))
            students = list(collection.find({"age": {"$gte": min_age, "$lte": max_age}}))
        except:
            students = []

    return render_template('Exercise15.html', students=students)

# Exercise 16: Filter by Gender
@app.route('/exercise16', methods=['GET'])
def exercise16():
    gender = request.args.get('gender')  # get gender from form
    if gender:
        students = list(collection.find({"gender": gender}))
    else:
        students = []
    return render_template('Exercise16.html', students=students)


if __name__ == "__main__":
    app.run(debug=True)
