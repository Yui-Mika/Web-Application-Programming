from flask import Flask, render_template, abort

app = Flask(__name__)

# Dictionary contains FAQ questions
faq_dict = {
    1: {"question": "What is Flask?", "answer": "Flask is a micro web framework written in Python."},
    2: {"question": "What is Python?", "answer": "Python is a high-level programming language."},
    3: {"question": "What is HTML?", "answer": "HTML is the standard markup language for documents designed to be displayed in a web browser."}
}

@app.route("/faq/<int:question_id>")
def faq(question_id):
    faq_entry = faq_dict.get(question_id)
    if faq_entry:
        return render_template("faq.html", question=faq_entry["question"], answer=faq_entry["answer"])
    else:
        abort(404, description="Question not found")

if __name__ == "__main__":
    app.run(debug=True)
