from flask import Flask, render_template, request

app = Flask(__name__)


VALID_COLORS = {"blue", "red", "green", "orange", "maroon",
                "navy", "gold", "purple", "black", "silver"}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        color = request.form.get("color")
        if color in VALID_COLORS:
            print("Form submitted!")
            return render_template("color.html", color=color)
        else:
            return "Invalid color!"
