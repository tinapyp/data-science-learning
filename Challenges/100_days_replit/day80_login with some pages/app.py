from flask import Flask, request, redirect, render_template

app = Flask(__name__)

account = {
    "test": {"username": "test", "password": "1234"},
    "testing": {"username": "testing", "password": "1234"},
    "testong": {"username": "testong", "password": "1234"},
}


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/failed")
def failed():
    return render_template("failed.html")


@app.route("/login", methods=["POST"])
def login():
    data = request.form
    input_username = data["username"]
    input_password = data["password"]
    if (
        input_username == account[input_username]["username"]
        and input_password == account[input_username]["password"]
    ):
        return redirect("/success")
    else:
        return redirect("/failed")


app.run(host="0.0.0.0", port=81, debug=True)
