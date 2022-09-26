# Chapter 43) Model API
---
## 1. API with Model

### 목표

- iris 데이터를 입력받아 예측할 수 있는 API를 작성합니다.

### 요구사항

1. `POST predict`/ & Request Body `{data}` 를 이용할 경우 모델의 예측값을 반환하는 API를 작성합니다.
    - API 명세서를 작성해봅니다.
2. `schemas.py` 에 Pydantic을 사용해 input_schema와 output_schema를 작성합니다.
    - input_schema: column 명은 앞선 db 챕터에서 작성한 이름을 기준으로 합니다.
    - output_schema
        - 모델의 결과를 `iris_class` 의 key값과 같이 반환합니다.
3. 작성한 내용으로 `crud.py`를 작성합니다.
4. 예측에 사용하는 모델은 mlflow에서 다운로드 받거나 바로 학습해서 사용해도 무관합니다.
    - 이 후 챕터에서는 mlflow에서 모델을 다운로드 받아서 사용하게 됩니다.
5. 작성된 `predict` API에 데이터를 전달해 예측값을 받아 봅니다.
---

## 2. Write data to DB

### 목표

- `predict` 로 요청받은 데이터와 그 결과를 DB에 저장합니다.

### 요구사항

1. `database.py` 를 작성해 db에 연결합니다.
2. `models.py` 를 작성합니다.
    - `raw_data` table columns:
        - 입력으로 받은 column들
        - `timestamp`: 요청받은 시간
    - `prediction` table columns:
        - `iris_class` 모델의 결과와
        - `timestamp`: 요청받은 시간
3. 작성한 내용으로 `crud.py` 를 수정합니다.
4. request를 날린후 `raw_data` table 과 `prediction` table을 확인합니다.
5. query문을 작성해 input 과 prediction 을 같이 확인합니다.

### 질문사항

1. 모델을 디버깅하기 위해서 입력값과 결과값을 머지하기 위해서는 어떻게 해야할까요?
    - `timestamp` or `uuid` ?
2. 왜 input_schema 와 output_schema가 필요할까요?

---
## 3. Docker with Model

### 목표

- 컨테이너에 모델 정보를 복사해 API를 띄우는 Dockerfile을 작성합니다.

### 요구사항

1. 작성한 API에 필요한 모델을 이미지에 복사하는 Dockerfile을 작성합니다.
    - 이 이미지를 실행하면 별도의 모델 정보를 요구하지 않습니다.
2. 빌드된 이미지를 실행합니다.
3. example을 통해 정상적으로 예측하는지 확인합니다.
4. DB에 데이터가 쌓이고 있는지 확인합니다.

---

## 4. Docker without Model

### 목표

- 모델 경로를 받아 API를 띄우는 Dockerfile을 작성합니다.

### 요구사항

1. 작성한 API에 필요한 모델을 `/mnt/models` 경로에서 가져오도록 코드를 수정합니다.
2. 빌드된 이미지를 실행합니다.
    - 모델이 있는 경로를 `/mnt/models` 로 volume mapping 합니다.
3. example을 통해 정상적으로 예측하는지 확인합니다.
4. DB에 데이터가 쌓이고 있는지 확인합니다.
