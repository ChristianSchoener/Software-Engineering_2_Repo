from flask import Flask, Response, request
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {"hello":"world"}

@app.route("/hello_world")
def hello_world_html():
    return "<p>Hello, World!</p>"

@app.route("/training_data")
def training_data():
  with open("data/auto-mpg.csv", "r") as f:
    content = f.read()
  return Response(content, mimetype="text/plain")

@app.route("/predict")
def predict():
  zylinder = request.args.get('zylinder', default = 8, type = float)
  ps = request.args.get('ps', default = 130, type = float)
  gewicht = request.args.get('gewicht', default = 3504, type = float)
  beschleunigung = request.args.get('beschleunigung', default = 12, type = float)
  baujahr = request.args.get('baujahr', default = 70, type = float)
  model = pickle.load(open("data/models/auto-mpg","rb"))

  prediction = model.predict(np.array([zylinder,ps,gewicht,beschleunigung,baujahr]).reshape(1,-1))
  return {"mpg": str(prediction[0])}

# http://127.0.0.1:5000/predict?zylinder=8&ps=130&gewicht=3504&beschleunigung=12&baujahr=70
