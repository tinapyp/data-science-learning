from flask import Flask, request, render_template
from src.users import Users, User
from flask import jsonify

app = Flask(__name__)
users = Users()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/auth", methods=["POST"])
def auth():
    form = request.form

    username = form["username"]
    password = form["password"]

    auth = users.auth_login(username, password)
    if auth:
        return "Login Berhasil"
    else:
        data = users.display_users()
        return jsonify(data)


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/add-user", methods=["POST"])
def add_user():
    form = request.form

    name = form["name"]
    username = form["username"]
    password = form["password"]

    users.add_user(User(name=name, username=username, password=password))
    data = users.display_users()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
