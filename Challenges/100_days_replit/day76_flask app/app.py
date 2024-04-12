from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static", template_folder="templates")


@app.route("/")
def main():
    page = """<html><body>
    <p><a href='/linktree' />Linktree</p>
    <p><a href='/portofolio' />Portofolio</p>
    </body></html>
    """
    return page


@app.route("/linktree")
def linktree():
    return render_template("linktree.html")


@app.route("/portofolio")
def portofolio():
    return render_template("portofolio.html")


app.run(debug=True)
