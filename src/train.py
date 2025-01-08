import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("data/auto-mpg.csv",delimiter=";")
X = data.loc[:, data.columns != "mpg"]
y = data["mpg"]
reg = LinearRegression().fit(X,y)

with open("data/models/auto-mpg","wb") as f:
  pickle.dump(reg, f)
