from pydantic import BaseModel


class PredictIn(BaseModel):
    sepal_width: float
    sepal_length: float
    petal_width: float
    petal_length: float


class PredictOut(BaseModel):
    iris_class: int
