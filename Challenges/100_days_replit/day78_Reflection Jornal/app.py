from flask import Flask

app = Flask(__name__)


@app.route("/<pageNumber>")
def main(pageNumber):
    thought = {"1": "Mudah sekali", "2": "Tidak sulit", "3": "Sangat simpel"}
    changeThought = thought.get(pageNumber)
    with open("template/index.html", "r") as file:
        print(pageNumber)
        page = file.read()
        page = page.replace("{pageNumber}", pageNumber)
        page = page.replace("{list2}", str(changeThought))
    return page


app.run(debug="on")
