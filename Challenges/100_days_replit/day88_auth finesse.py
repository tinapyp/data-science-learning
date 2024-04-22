from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    if not request.headers["X-Replit-User-Name"]:
        page = """
        <!DOCTYPE html>
<html lang="en">
<head>
  
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hello There!</title>
<script src="https://replit.com/public/js/repl-auth-v2.js"></script>
</head>
<body>
  <h1>Here's my site</h1>
  <p>Go Login to see what inside</p>
  <button onclick="LoginWithReplit()"> Login </button>
</body>
</html>
        """
        f = open("templates/page.html", "r")
        page = f.read()
        f.close()
        return page
    elif request.headers["X-Replit-User-Id"] == "22601135":
        return "hello admin"
    else:
        return "hello user"


app.run(host="0.0.0.0", port=81)
