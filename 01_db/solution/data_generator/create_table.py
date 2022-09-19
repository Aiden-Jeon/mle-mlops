import psycopg2


def create_table(db_connect):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS iris_data (
        id SERIAL PRIMARY KEY,
        sepal_width float8,
        sepal_length float8,
        petal_width float8,
        petal_length float8,
        target int
    );"""
    print(create_table_query)
    with db_connect.cursor() as cur:
        cur.execute(create_table_query)
        db_connect.commit()


if __name__ == "__main__":
    db_connect = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="mypassword")
    create_table(db_connect)
