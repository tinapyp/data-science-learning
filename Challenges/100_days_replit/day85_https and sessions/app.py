from flask import Flask, request, render_template, session, redirect
from src.users import Users, User
from flask import jsonify
import os

app = Flask(__name__)
app.secret_key = os.environ["SESSION_KEY"]
users = Users()


def set_session(username):
    session["session"] = username
    return redirect("/")


@app.route("/")
def home():
    if session.get("session"):
        f = open("templates/page.html", "r")
        page = f.read()
        page = page.replace("{username}", session["session"])
        return page
    return render_template("index.html")


@app.route("/login")
def login():
    if session.get("session"):
        f = open("templates/page.html", "r")
        page = f.read()
        page = page.replace("{username}", session["session"])
        return page
    return render_template("login.html")


@app.route("/auth", methods=["POST"])
def auth():
    form = request.form

    username = form["username"]
    password = form["password"]

    auth = users.auth_login(username, password)
    if auth:
        set_session(username)
        return redirect("/")
    else:
        return "Login Gagal, Coba lagi Bruh!"


@app.route("/signup")
def signup():
    if session.get("session"):
        f = open("templates/page.html", "r")
        page = f.read()
        page = page.replace("{username}", session["session"])
        return page
    return render_template("signup.html")


@app.route("/add-user", methods=["POST"])
def add_user():
    form = request.form

    name = form["name"]
    username = form["username"]
    password = form["password"]

    users.add_user(User(name=name, username=username, password=password))
    return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
