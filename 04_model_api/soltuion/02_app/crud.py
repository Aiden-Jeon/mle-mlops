import os
from datetime import datetime

import mlflow
import pandas as pd
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, DataIn, DataOut
from schemas import PredictIn, PredictOut

Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


MODEL = mlflow.pyfunc.load_model("../model")


@app.post("/predict", response_model=PredictOut)
def predict(data: PredictIn, db: Session = Depends(get_db)):
    now = datetime.utcnow()

    df = pd.DataFrame([data.dict()])
    pred = int(MODEL.predict(df))

    data_in = DataIn(timestamp=now, **data.dict())
    db.add(data_in)
    db.commit()
    db.refresh(data_in)

    data_out = DataOut(timestamp=now, iris_class=pred)
    db.add(data_out)
    db.commit()
    db.refresh(data_out)
    return PredictOut(iris_class=pred)
