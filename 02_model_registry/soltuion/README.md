# Model Reigstry
## Mlflow Server

`mlflow` 를 설치합니다.
```bash
pip install mlflow
```

mlflow server를 동작합니다.
```bash
mlflow server
```

## Train
모델을 학습 후 mlflow server에 저장합니다.

```bash
python train.py
```

## Load
다음 스크립트를 이용해 run_id 목록을 확인합니다.

```bash
python list_run.py
```

실행 후 다음과 같은 값이 출력됩니다.

```bash
> python list_run.py
8893c67cc1a44a29bc38bdde4559508c
```

모델을 load 할 run id를 입력해 모델을 로드합니다.
```bash
python load.py --run-id=<RUN_ID>
```
