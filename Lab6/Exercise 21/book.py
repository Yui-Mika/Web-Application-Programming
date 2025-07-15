from flask import Flask, render_template, request

app = Flask(__name__)

#List of books
books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "1984", "author": "George Orwell"}
]

@app.route("/books", methods=["GET", "POST"])
def book_list():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        books.append({"title": title, "author": author})
        return render_template("books.html", books=books)
    
    return render_template("books.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)
