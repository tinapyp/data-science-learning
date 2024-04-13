from flask import Flask
import datetime as dt

app = Flask(__name__)


@app.route("/")
def home():
    time = dt.date.today()
    with open("template/portfolio.html", "r") as file:
        page = file.read()
        page = page.replace("{datetime}", str(time))
    return page


app.run(host="0.0.0.0", port=81)
