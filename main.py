import joblib

from typing import List
from fastapi import FastAPI


app = FastAPI()

model = joblib.load('model.joblib')

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.post('/predict/')
def predict(features: List[float]):

    prediction = model.predict([features])

    return {"prediction": prediction.tolist()[0]}

