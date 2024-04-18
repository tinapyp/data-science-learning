from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
  data = request.args
  if data["lang"].lower() == "eng":
    return "Hello, my friend from wordwide"
  elif data['lang'].lower() == 'ind':
    return "Halo, temanku dari dunia"


app.run(host='0.0.0.0', port=81)
