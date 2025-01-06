import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("auto-mpg.csv",delimiter=";")
X = data.loc[:, data.columns != "baujahr"]
y = data["baujahr"]
reg = LinearRegression().fit(X,y)

with open("./models/auto-mpg-baujahr","wb") as f:
  pickle.dump(reg, f)