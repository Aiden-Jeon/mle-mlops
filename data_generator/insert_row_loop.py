import time
import pandas as pd
import psycopg2
from sklearn.datasets import load_iris


def get_data():
    X, y = load_iris(return_X_y=True, as_frame=True)
    df = pd.concat([X, y], axis="columns")
    rename_rule = {
        "sepal length (cm)": "sepal_width",
        "sepal width (cm)": "sepal_length",
        "petal length (cm)": "petal_width",
        "petal width (cm)": "petal_length",
    }
    df = df.rename(columns=rename_rule)
    return df


def insert_row(db_connect, data):
    insert_row_query = f"""
    INSERT INTO iris_data
        (sepal_width, sepal_length, petal_width, petal_length, target)
        VALUES (
            {data.sepal_width.values[0]},
            {data.sepal_length.values[0]},
            {data.petal_width.values[0]},
            {data.petal_length.values[0]},
            {data.target.values[0]}
        );
    """
    print(insert_row_query)
    with db_connect.cursor() as cur:
        cur.execute(insert_row_query)
        db_connect.commit()


def insert_row_loop(db_connect, df):
    while True:
        insert_row(db_connect, df.sample(1))
        time.sleep(5)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--host")
    args = parser.parse_args()
    db_connect = psycopg2.connect(host=args.host, database="postgres", user="postgres", password="mypassword")
    df = get_data()
    insert_row_loop(db_connect, df.sample(1))
