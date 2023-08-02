import pickle
from src.data import featureAddition # This import is necessary for the pickle load featureAddition()

with open ("assets/data_pipe.pkl",'rb') as f:
    data_pipe=pickle.load(f)
    
with open ("assets/model.pkl",'rb') as f:
    model=pickle.load(f)

def run(data):
    return model.predict(data_pipe.transform(data))