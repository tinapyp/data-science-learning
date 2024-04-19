from flask import Flask, render_template, request

app = Flask(__name__)

themes = {
    "black": """*{
    background-color: black;
}

h1{
    color:white
}

#current_date {
    color: white;
    font-family: Arial, sans-serif;
}


#text{
    color: white;
    font-family: Arial, sans-serif;
}
""",
    "white": """*{
    background-color: white;
}

h1{
    color:black
}

#current_date {
    color: black;
    font-family: Arial, sans-serif;
}


#text{
    color: black;
    font-family: Arial, sans-serif;
}
""",
}


def write_file(data):
    with open("static/css/style.css", "w") as file:
        file.write(data)
        file.close()


def change_theme(theme):
    data = themes.get(theme)
    write_file(data)


@app.route("/hello", methods=["GET"])
def home():
    data = request.args
    print(data)
    if not data:
        change_theme("black")
    else:
        change_theme(data["theme"])
    return render_template("index.html")


app.run(debug=True)
