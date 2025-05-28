from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    student = {
        "name": "Duong Ngoc Linh Dan",
        "student_id": "2374802010091",
        "academic_year": "2nd year",
        "major": "Information Technology",
        "hobbies": ["Reading books", "Watching Films", "Listening to Music"],
    }
    return render_template('student.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)