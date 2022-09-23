# API
## Install
fastapi 를 설치합니다.
```bash
pip install "fastapi[all]"
```

## FastAPI Tutorial

```bash
uvicorn tutorial.tutorial:app --reload
```

## FastAPI CRUD

```bash
uvicorn tutorial.crud:app --reload
```

## FastAPI CRUD with Pydantic

```bash
uvicorn tutorial.crud_pydantic:app --reload
```

## Docker

```bash
docker-compose up -d --build
```
