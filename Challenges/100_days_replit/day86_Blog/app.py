import os
from flask import Flask
from flask import redirect, request, render_template, session, jsonify
from src.utils import authentication, save_data, read_data, read_data_html

app = Flask(__name__)
app.secret_key = os.environ["SESSION_KEY"]


def set_session(username: str) -> None:
    session["session"] = username
    return redirect("/page")


@app.route("/")
def index():
    if session.get("session"):
        return redirect("/page")
    path = "data/post.txt"
    posts: list = read_data(path)
    page = ""
    for post in posts:
        page += "<p>" + post["title"] + "</p>"
        page += "<p>" + post["date"] + "</p>"
        page += "<p>" + post["article"] + "</p>"
        page += "<hr><br>"
    data = read_data_html("templates/index.html")
    data = data.replace("{POST}", page)
    return data


@app.route("/page")
def page():
    path = "data/post.txt"
    posts: list = read_data(path)
    page = ""
    for post in posts:
        page += "<p>" + post["title"] + "</p>"
        page += "<p>" + post["date"] + "</p>"
        page += "<p>" + post["article"] + "</p>"
        page += "<hr><br>"
    data = read_data_html("templates/page.html")
    data = data.replace("{POST}", page)
    return data


@app.route("/add-post", methods=["POST"])
def add_post():
    new_post = dict(request.form)
    path = "data/post.txt"
    while True:
        try:
            posts: list = read_data(path)
            break
        except:
            save_data(path)

    posts.append(new_post)
    save_data(path, str(posts))
    return redirect("/page")


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@app.route("/auth-login", methods=["POST"])
def auth_login():
    data = request.form
    username = data["username"]
    password = data["password"]
    auth = authentication(username=username, password=password)
    if auth:
        set_session(username=username)
        return redirect("/page")
    else:
        return redirect("/login")


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect("/")


app.run(debug=True)
