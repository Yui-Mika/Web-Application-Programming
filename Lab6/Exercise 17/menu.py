from flask import Flask, render_template, abort

app = Flask(__name__)

# Dictionary contains menus for categories
menu = {
    "drinks": [{"name": "Coffee", "price": 2}, {"name": "Tea", "price": 1.5}],
    "food": [{"name": "Burger", "price": 5}, {"name": "Pizza", "price": 8}]
}

@app.route("/menu/<category>")
def show_menu(category):
    if category in menu:
        return render_template("menu.html", category=category, items=menu[category])
    else:
        abort(404, description="Category not found")

if __name__ == "__main__":
    app.run(debug=True)
