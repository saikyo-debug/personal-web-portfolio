from datetime import date

from flask import Flask, render_template

import data

app = Flask(__name__)

NAV = [
    ("home", "Home"), ("about", "About"), ("skills", "Skills"),
    ("projects", "Projects"), ("experience", "Experience"),
    ("fieldwork", "Field work"), ("education", "Education"),
    ("contact", "Contact"),
]


@app.route("/")
def index():
    return render_template("index.html", nav=NAV, year=date.today().year, **data.CONTENT)


if __name__ == "__main__":
    app.run(debug=True)
