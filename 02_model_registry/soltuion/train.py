import mlflow
import pandas as pd
import psycopg2
from sklearn.svm import SVC


def get_data():
    db_connect = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="mypassword")
    df = pd.read_sql("SELECT * FROM iris_data ORDER BY id DESC LIMIT 10", db_connect)
    return df


def train(df):
    X = df.drop(["id", "target"], axis="columns")
    y = df["target"]
    classifier = SVC()
    classifier.fit(X, y)
    return classifier


def log_model(model):
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.sklearn.log_model(model, "iris_model")


if __name__ == "__main__":
    df = get_data()
    model = train(df)
    log_model(model)
