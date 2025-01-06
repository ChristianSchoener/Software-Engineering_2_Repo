import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
import sys

model = pickle.load(open("./models/auto-mpg-baujahr","rb"))

mpg = float(sys.argv[1])
zylinder = float(sys.argv[2])
ps = float(sys.argv[3])
gewicht = float(sys.argv[4])
beschleunigung = float(sys.argv[5])

print("Baujahr-Prediction:",model.predict(np.array([mpg,zylinder,ps,gewicht,beschleunigung]).reshape(1,-1)))