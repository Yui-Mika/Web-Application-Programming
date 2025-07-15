from flask import Flask, render_template, abort

app = Flask(__name__)

# Dictionary contains blog posts
posts = {
    1: {"title": "First Post", "content": "Hello World!"},
    2: {"title": "Second Post", "content": "Flask is awesome!"},
    3: {"title": "Third Post", "content": "Python is great!"}
}

@app.route("/post/<int:post_id>")
def post(post_id):
    post = posts.get(post_id)
    if post:
        return render_template("blog.html", title=post["title"], content=post["content"])
    else:
        abort(404, description="Post not found")

if __name__ == "__main__":
    app.run(debug=True)
