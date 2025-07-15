from flask import Flask, render_template
import random

app = Flask(__name__)

# List of quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "Be the change that you wish to see in the world. - Mahatma Gandhi"
]

@app.route("/quote")
def quote():
    # Pick a random sentence
    selected_quote = random.choice(quotes)
    return render_template("quote.html", quote=selected_quote)

if __name__ == "__main__":
    app.run(debug=True)
