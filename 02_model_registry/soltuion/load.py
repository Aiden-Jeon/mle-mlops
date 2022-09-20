import os
import mlflow

os.makedirs("download", exist_ok=True)


def download_model(run_id):
    client = mlflow.MlflowClient("http://localhost:5000")
    artifact = client.list_artifacts(run_id)[0].path
    dst_path = "download"
    client.download_artifacts(run_id=run_id, path=artifact, dst_path=dst_path)
    dst_path += "/" + artifact
    return dst_path


def load_model(dst_path):
    model = mlflow.pyfunc.load_model(dst_path)
    return model


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--run-id", type=str)
    args = parser.parse_args()
    
    dst_path = download_model(args.run_id)
    model = load_model(dst_path)
