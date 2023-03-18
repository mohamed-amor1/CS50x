# Implements a registration form, storing registrants in a SQLite database, with support for deregistration

import sqlite3
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/deregister", methods=["POST"])
def deregister():

    # Forget registrant
    id = request.form.get("id")
    if id:
        with sqlite3.connect("froshims.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM registrants WHERE id = ?", (id,))
    return redirect("/registrants")


@app.route("/register", methods=["POST"])
def register():

    # Validate submission
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name or sport not in SPORTS:
        return render_template("failure.html")

    # Remember registrant
    with sqlite3.connect("froshims.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO registrants (name, sport) VALUES (?, ?)", (name, sport))
        # Confirm registration
        return redirect("/registrants")


@app.route("/registrants")
def registrants():
    with sqlite3.connect("froshims.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM registrants")
        rows = cursor.fetchall()
        registrants = [dict(id=row[0], name=row[1], sport=row[2]) for row in rows]
        return render_template("registrants.html", registrants=registrants)
