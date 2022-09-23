# Chapter 02) Model Registry
---
## 1. MLFlow Server 띄우기
### 목표

- 로컬에서 MLFLow Server를 띄어봅시다.

### 요구사항

1. 로컬에 mlflow server를 띄웁니다.
    - `mlflow server` 를 사용해 서버를 띄웁니다.
    - mlflow server는 “3.모델 학습 및 저장” 와 작성할 스크립트와 같은 디렉토리에서 실행되어야 합니다.
2. mlflow ui website를 확인합니다.

---
## 2. 데이터 추출
### 목표

- 앞선 챕터에서 만든 DB에서 데이터를 추출합니다.

### 요구사항

1. `pandas.read_sql` 함수를 이용합니다.
2. `id` column을 기준으로 최신 데이터 100개를 추출하는 쿼리문을 작성합니다.
3. 데이터를 추출합니다.

---
## 3. 모델 학습 및 저장

### 목표

- 모델을 학습하고 mlflow server에 저장합니다.

### 요구사항

1. 앞선 챕터에서 추출한 데이터를 이용해 모델을 학습합니다.
    - eg) `from sklearn.svm import SVC`
    - 모델을 학습하는 스크립트의 위치는 mlflow server 가 띄어진 위치와 같아야 합니다.
        
        ```
        .
        ├── mlruns
        │   └── 0
        │       └── meta.yaml
        └── train.py
        ```
        
2. 학습이 끝난 모델을 built-in method를 사용해 mlflow server에 저장합니다.
    - Python의 `mlflow` 패키지를 이용합니다.
        - `pip install mlflow`
    - mlflow를 이용해 logging 하는 방법은 두 가지가 있습니다.
        1. fluent
        2. client [[MLFlow Client](https://www.mlflow.org/docs/latest/python_api/mlflow.client.html)]
    - mlflow에는 모델을 저장하는 방법은 두 가지가 있습니다.
        - artifact 처럼 다루기 [[MLFLow log_artifact](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.log_artifact)]
        - built-in method 사용하기
            - [MLFlow built-in Model Flavors](https://www.mlflow.org/docs/latest/models.html#built-in-model-flavors)
            - [MLFLow pyfunc log_model](https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#mlflow.pyfunc.log_model)
3. 저장된 모델을 mlflow website에서 확인합니다.
    - 모델이 어떻게 저장되어 있는지 확인합니다. [[MLFlow Storage Format](https://www.mlflow.org/docs/latest/models.html#storage-format)]

---
## 4. Download Model from MLFlow

### 목표

- mlflow에 저장된 모델을 다운로드 받을 수 있는 스크립트를 작성합니다.

### 요구사항

1. run id를 입력하면 mlflow에 저장된 모델을 다운로드 받을 수 있는 스크립트를 작성합니다.
    - python sdk: `mlflow.MlflowClient`
    - bash: `rclone`
2. 앞선 챕터에서 로깅된 run_id를 이용해 모델을 다운로드 합니다.
3. 다운로드 받은 모델을 `mlflow.pyfunc.load_model` 을 이용해 load 합니다.
