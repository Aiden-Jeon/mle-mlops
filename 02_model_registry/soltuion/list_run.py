import mlflow


def list_run(experiment_id=0):
    client = mlflow.MlflowClient("http://localhost:5000")
    runs = client.list_run_infos(experiment_id=experiment_id)
    run_ids = [run.run_id for run in runs]
    print("\n".join(run_ids))
    return run_ids


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--experiment-id", default=0, type=int)
    args = parser.parse_args()
    list_run(args.experiment_id)
