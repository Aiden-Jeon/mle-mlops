import mlflow
import pandas as pd
from fastapi import FastAPI

from schemas import PredictIn, PredictOut

app = FastAPI()

MODEL = mlflow.pyfunc.load_model("../model")


@app.post("/predict", response_model=PredictOut)
def predict(data: PredictIn):
    df = pd.DataFrame([data.dict()])
    pred = int(MODEL.predict(df))
    return PredictOut(iris_class=pred)
