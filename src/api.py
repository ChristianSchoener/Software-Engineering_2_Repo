from flask import Flask, Response
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {"hello":"world"}

@app.route("/hello_world")
def hello_world_html():
    return "<p>Hello, World!</p>"

@app.route("/training_data")
def train_data():
  with open("data/auto-mpg.csv", "r") as f:
    content = f.read()
  return Response(content, mimetype="text/plain")
