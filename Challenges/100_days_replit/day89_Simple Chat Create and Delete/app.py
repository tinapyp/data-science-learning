import random
import os
from flask import Flask
from flask import request, render_template, redirect, session

app = Flask(__name__)
app.secret_key = os.environ["SESSION_SECRET"]

chats = []


def set_session():
    session["session"] = request.headers["X-Replit-User-Id"]


def get_chats():
    chat_html = ""
    for data in chats:
        chat_html += "<div><hr>"
        chat_html += f"<p>User ID: {data['chat_id']}</p>"
        chat_html += f"<p>Chat: {data['text']}</p>"
        chat_html += f"<form action='/delete-chat' method='post'>"
        chat_html += f"<input type='hidden' name='chat_id' value='{data['chat_id']}'>"
        chat_html += f"<button type='submit'>Delete</button>"
        chat_html += "</form>"
        chat_html += "</div>"
    return chat_html


@app.route("/")
def home():
    if "session" not in session:
        set_session()
        return render_template("login.html")
    else:
        return redirect("/page")


@app.route("/page")
def page():
    page = ""
    chat = get_chats()
    f = open("templates/page.html", "r")
    page = f.read()
    page = page.replace("{Name}", request.headers["X-Replit-User-Name"])
    page = page.replace("{Chat}", chat)
    return page


@app.route("/add-chat", methods=["POST"])
def add_post():
    chat_id = str(random.randint(1, 10000))
    user_id = session.get("session")
    text = request.form["text"]

    chat = {"user_id": user_id, "chat_id": chat_id, "text": text}
    chats.append(chat)
    return redirect("/page")


@app.route("/delete-chat", methods=["POST"])
def delete_post():
    chat_id_to_remove = request.form["chat_id"]
    idx_to_remove = None

    for idx, chat in enumerate(chats):
        if chats[idx]["chat_id"] == chat_id_to_remove:
            idx_to_remove = idx
            print(idx_to_remove)
            break

    if idx_to_remove is not None:
        del chats[idx_to_remove]

    return redirect("/page")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


app.run(debug=True)
