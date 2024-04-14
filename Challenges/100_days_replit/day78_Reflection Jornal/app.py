from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return redirect("/1")


@app.route("/<pageNumber>")
def tree(pageNumber):
    thought = {"1": "Mudah sekali", "2": "Tidak sulit", "3": "Sangat simpel"}
    changeThought = thought.get(pageNumber)
    try:
        with open("template/journal.html", "r") as file:
            print(pageNumber)
            page = file.read()
            page = page.replace("{pageNumber}", pageNumber)
            page = page.replace("{list2}", str(changeThought))
        return page
    except:
        return redirect("/")


app.run(debug="on")
