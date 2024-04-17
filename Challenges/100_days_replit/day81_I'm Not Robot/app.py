from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/robot", methods=["POST"])
def robot():
    data = request.form
    if (
        data["food"] == "human food"
        and data["metal"] == "no"
        and data["number"] == "no idea"
    ):
        return "Welcome Human!"
    else:
        return "You're Robot!!!"


app.run(debug=True)
