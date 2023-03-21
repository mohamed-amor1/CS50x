import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure flask to use the "birthdays.db" database with sqlalchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Mohamed/Desktop/COMPUTER SCIENCE/cs50/CS50x/week-9-flask/labs/birthdays/birthdays.db'
db = SQLAlchemy(app)

# define a model for the "birthdays" table using the SQLAlchemy ORM.


class Birthdays(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        new_birthday = Birthdays(name=name, month=month, day=day)
        db.session.add(new_birthday)
        db.session.commit()

        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        birthdays = Birthdays.query.all()
        return render_template("index.html", birthdays=birthdays)


if __name__ == '__main__':
    app.run(debug=True)
