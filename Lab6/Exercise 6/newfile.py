from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        # Do not save file, only display selected file name
        return f"File uploaded: {file.filename}"
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)