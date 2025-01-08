import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
import sys

model = pickle.load(open("data/models/auto-mpg","rb"))

zylinder = float(sys.argv[1])
ps = float(sys.argv[2])
gewicht = float(sys.argv[3])
beschleunigung = float(sys.argv[4])
baujahr = float(sys.argv[5])


print("mpg-prediction:",model.predict(np.array([zylinder,ps,gewicht,beschleunigung,baujahr]).reshape(1,-1)))
