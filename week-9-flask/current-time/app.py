from flask import Flask, render_template
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

@app.route("/")
def time():
    cambridge_time = timezone("America/New_York")
    now = datetime.now(cambridge_time)
    date_string = now.strftime("%A, %B %d, %Y") # format the date as "Monday, January 01, 2022"
    eastern_time = timezone("America/New_York")
    amsterdam = timezone("Europe/Amsterdam")
    now = datetime.now(eastern_time)
    now2 = datetime.now(amsterdam)
    return render_template("index.html",date=date_string, now=now, now2=now2) 

if __name__ == "__main__":
    app.run(debug=True)
