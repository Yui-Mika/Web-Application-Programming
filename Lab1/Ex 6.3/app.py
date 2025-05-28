from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def student_form():
        student_name = "Linh Dan"
        submitted = False
        data = {}
        if request.method == 'POST':
            submitted = True
            data = request.form.to_dict()
        return render_template('form.html', student_name=student_name, submitted=submitted, data=data)

if __name__ == '__main__':
    app.run(debug=True)


        


