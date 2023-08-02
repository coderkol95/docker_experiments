from sklearn.linear_model import LinearRegression
import pandas as pd
import pickle
from data import featureAddition # This import is necessary for the pickle load featureAddition()

with open ("assets/data_pipe.pkl",'rb') as f:
    data_pipe=pickle.load(f)

model = LinearRegression()

X = pd.read_csv("data/features.csv")
y = pd.read_csv("data/target.csv")

X = data_pipe.transform(X)

model.fit(X,y)

with open ("assets/model.pkl",'wb') as f:
    pickle.dump(model,f)