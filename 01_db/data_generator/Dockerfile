FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip &&\
    pip install psycopg2-binary scikit-learn pandas

COPY insert_row_loop.py insert_row_loop.py

ENTRYPOINT ["python", "insert_row_loop.py", "--host"]
