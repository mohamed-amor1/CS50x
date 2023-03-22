import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'


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
        # Validate user input
        name = request.form.get("name")
        if not name or len(name) > 50 or not name.isalpha():
            flash(
                "Invalid name format. Please enter a string with maximum 50 characters.")
            return redirect("/")

        try:
            month = int(request.form.get("month"))
            if not 1 <= month <= 12:
                raise ValueError()
        except (ValueError, TypeError):
            flash(
                "Invalid month value. Please enter a positive integer between 1 and 12.")
            return redirect(request.url)

        try:
            day = int(request.form.get("day"))
            if not 1 <= day <= 31:
                raise ValueError()
        except (ValueError, TypeError):
            flash("Invalid day value. Please enter a positive integer between 1 and 31.")
            return redirect(request.url)

       # Add the user's entry into the database
        new_birthday = Birthdays(name=name, month=month, day=day)
        db.session.add(new_birthday)
        db.session.commit()
        flash("Birthday added successfully.")

        return redirect("/")

    edit_id = request.args.get("edit_id")
    if edit_id:
        # Retrieve the corresponding entry from the database
        birthday = Birthdays.query.get(edit_id)
        if birthday:
            # Display the edit form for the entry
            return render_template("index.html", birthday=birthday, edit_mode=True)
        else:
            flash("Invalid birthday ID.")

    else:

        # TODO: Display the entries in the database on index.html
        birthdays = Birthdays.query.order_by(Birthdays.month).all()
        return render_template("index.html", birthdays=birthdays)


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    birthday = Birthdays.query.get_or_404(id)
    db.session.delete(birthday)
    db.session.commit()
    flash("Birthday entry deleted successfully.")
    return redirect("/")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    birthday = Birthdays.query.get_or_404(id)

    if request.method == "POST":
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # Validate input
        errors = []
        if not name or len(name) > 50:
            errors.append(
                "Name should be a string with maximum 50 characters.")
        if not month or not month.isdigit() or int(month) < 1 or int(month) > 12:
            errors.append(
                "Month should be a positive integer between 1 and 12.")
        if not day or not day.isdigit() or int(day) < 1 or int(day) > 31:
            errors.append("Day should be a positive integer between 1 and 31.")

        # If input is valid, update the entry and redirect to home page
        if not errors:
            birthday.name = name
            birthday.month = month
            birthday.day = day
            db.session.commit()
            flash("Birthday updated successfully.")
            return redirect("/")

        # If input is not valid, show error messages and reload the form
        for error in errors:
            flash(error)

    # Render the edit form
    return render_template("index.html", edit_mode=True, bday=birthday)


if __name__ == '__main__':
    app.run(debug=True)
