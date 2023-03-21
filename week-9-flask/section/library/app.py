from flask import Flask, render_template, request
from helpers import random_string
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Mohamed/Desktop/COMPUTER SCIENCE/cs50/CS50x/week-9-flask/section/library/history.db'

db = SQLAlchemy(app)


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.Integer)

    def __init__(self, page):
        self.page = page


app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        page = request.form.get("page")

        try:
            page = int(page)
        except ValueError:
            return render_template("index.html", random_string="Enter a number!")

        if page < 0:
            return render_template("index.html", random_string="Enter a positive number!")

        with app.app_context():
            db.session.add(History(page))
            db.session.commit()

        random.seed(page)

    string = random_string(2000)
    history = History.query.all()
    return render_template("index.html", random_string=string, history=history)


if __name__ == '__main__':
    app.run(debug=True)


# random.seed is a function in Python's random module that is used to initialize the random number generator with a given seed value. When the random number generator is initialized with a seed value, it will always produce the same sequence of pseudo-random numbers for a given seed.
# In Flask, random.seed can be used to generate pseudo-random numbers for various purposes, such as generating random tokens, session IDs, or passwords.
