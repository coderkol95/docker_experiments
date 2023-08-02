from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pickle
import pandas as pd

X = pd.read_csv("data/features.csv")
y = pd.read_csv("data/target.csv")

class featureAddition(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):

        return self

    def transform(self, X):

        X[:,2]=X[:,2]+X[:,3] # Adding last two features
        return X[:,:2]
    
data_pipe=Pipeline([('standardScaler',StandardScaler()),('featureAddition',featureAddition())])
fitted_pipe=data_pipe.fit(X)
with open('assets/data_pipe.pkl','wb') as f:
    pickle.dump(fitted_pipe,f)
