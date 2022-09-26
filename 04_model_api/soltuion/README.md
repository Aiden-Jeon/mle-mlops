# Chapter 04) Model API

## Download model
`load.py` 를 이용해 해당 디렉토리에 model 을 다운로드 합니다.

## API with Model
01_app 폴더로 이동후 실행시킵니다.
```bash
cd 01_app
uvicorn crud:app --reload
```

## Write Data to DB
02_app 폴더로 이동후 실행시킵니다.

```bash
cd 02_app
uvicorn crud:app --reload
```

## Docker with Model
이미지를 빌드합니다.

```bash
docker build -f ./03_Dockerfile -t docker_with_model
```

빌드된 이미지를 실행합니다.

```bash
docker run docker_with_model
```

## Docker without Model
이미지를 빌드합니다.

```bash
docker build -f ./04_Dockerfile -t docker_with_model
```

빌드된 이미지를 실행합니다.

```bash
docker run -p $(pwd)/model:/mnt/models docker_without_model
```
