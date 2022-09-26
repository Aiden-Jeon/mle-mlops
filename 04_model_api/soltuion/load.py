import os

import mlflow
from sklearn.datasets import load_iris

os.makedirs("download", exist_ok=True)


def get_sample():
    df, _ = load_iris(return_X_y=True, as_frame=True)
    rename_rule = {
        "sepal length (cm)": "sepal_width",
        "sepal width (cm)": "sepal_length",
        "petal length (cm)": "petal_width",
        "petal width (cm)": "petal_length",
    }
    df = df.rename(columns=rename_rule)
    return df.sample(1)


def download_model(run_id):
    client = mlflow.MlflowClient("http://localhost:5000")
    artifact = client.list_artifacts(run_id)[0].path
    dst_path = "download"
    client.download_artifacts(run_id=run_id, path=artifact, dst_path=dst_path)
    dst_path += "/" + artifact
    return dst_path


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--run-id", type=str)
    args = parser.parse_args()

    dst_path = download_model(args.run_id)
