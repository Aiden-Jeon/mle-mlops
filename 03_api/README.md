# Chapter 03) API
---
## 0. Restful API
### 목표

- Restful API가 무엇인지 학습합니다.
- OpenAPI 란 무엇인지 학습합니다.

---
## 1. FastAPI Tutorial
### 목표

- fast api tutorial을 따라합니다.

### 요구사항

1. [Tutorial User Guid - Intro](https://fastapi.tiangolo.com/tutorial/)
2. [First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)

---
## 2. FastAPI CRUD
### 목표

- FastAPI를 이용해 CRUD가 되는 api를 작성합니다.
- Path Parameter 와 Query Parameter의 차이점을 알아봅니다.

### 요구사항

1. 다음의 CRUD를 수행하는 fastapi의 명세서를 작성합니다.
    - Create: 이름과 별명을 입력할 수 있습니다.
    - Read: 이름을 입력하면 별명을 얻을 수 있습니다.
        - 만약 입력된 이름이 없다면 `400 code` 와 함께 `Name not found` 메세지를 반환합니다.
        - 이를 위해서 `fastapi.HTTPException` 를 사용합니다. [[FastAPI Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)]
    - Update: 이름과 새로운 별명을 입력하면 이름의 별명이 업데이트 됩니다.
        - 만약 입력된 이름이 없다면 `400 code` 와 함께 `Name not found` 메세지를 반환합니다.
    - Delete: 이름을 입력하면 해당 이름과 별명을 삭제합니다.
        - 만약 입력된 이름이 없다면 `400 code` 와 함께 `Name not found` 메세지를 반환합니다.
2. 작성한 명세서를 구현합니다.
    - API에 필요한 정보들은 메모리에 저장합니다.
3. fastapi의 swagger에서 다음 시나리오를 확인합니다.
    1. `{"name": "hello2", "nickname": "world"}` 로 create 합니다.
    2. `{"name": "hello2", "nickname": "world"}` 로 update 합니다.
        - 에러가 발생하는지 확인합니다.
    3. `{"name": "hello"}` 로 read 합니다.
        - 정상적으로 `“world"` 를 반환하는 지 확인합니다.
    4. `{"name": "hello", "nickname": "world"2}` 로 update 합니다.
    5. 주어`{"name": "hello"}` 로 read 합니다.
        - 정상적으로 `“world2"` 를 반환하는 지 확인합니다.
    6. `{"name": "hello"}` 로 delete 합니다.
    7. `{"name": "hello"}` 로 read합니다.
4. Path Parameter 와 Query Parameter의 차이점은 무엇인가요?

### 명세서 예시

이름과 별명을 입력받는 명세서

- Path Parameter
    - Request Header
        - `POST /example_1`
    - Request Body
        
        ```json
        {
          "name": "hello",
          "nickname": "world"
        }
        ```
        
    - Response
        
        ```json
        {
          "status": "success"
        }
        ```
        
- Query Parameter
    - Request Header
        - `POST /example_2/name/{name}/nickname/{nickname}`
    - Request Body
        
        ```json
        {}
        ```
        
    - Response

---
## 3. FastAPI CRUD + Pydantic

### 목표

- 앞서 작성한 API 코드를 pydantic을 이용해 작성합니다.

### 요구사항

1. 앞서 작성한 Create API를 Path Parameter로 작성합니다.
2. Create API에서 입력으로 받아야 하는 값들을 `pydantic.BaseModel` 로 수정합니다. [[Request Body](https://fastapi.tiangolo.com/tutorial/body/)]
    - `Class CreateIn(BaseModel):`
3. create 함수를 수정합니다. [[Use the model](https://fastapi.tiangolo.com/tutorial/body/#use-the-model)]
4. create 후 반환하는 값을 Response Model로 수정합니다. [[Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)]
    - `Class CreateOut(BaseModel):`
    - status, id 를 반환합니다.
        - id는 memory에 들어있는 length를 반환합니다.
        - eg) 첫 번째 입력값의 id는 0입니다.
5. create 함수의 반환 값을 ResponseModel로 수정합니다.
6. Pydantic으로 작성하기 전과 후의 api의 차이점을 비교합니다.

---
## 4. FastAPI + Postgresql
### 목표

- 앞서 작성한 fastapi의 정보를 postgesql db에 작성합니다.

### 요구사항

1. Postgresql 서버를 실행합니다.
    - 데이터가 저장되고 있는 도커와는 다른 서버를 실행해주세요.
    - 포트가 사용중이라면 5433 으로 포워딩합니다.
2. 다음 과정에 따라 create 함수로 입력 받는 값을 postgresql 에 저장하게 합니다.
    1. ORM(Object Relational Mapping) 에 대해서 알아봅니다. [[ORMs](https://fastapi.tiangolo.com/tutorial/sql-databases/?h=pydantic#orms)]
    2. `database.py` 파일을 생성합니다.[[File Structure](https://fastapi.tiangolo.com/tutorial/sql-databases/?h=pydantic#file-structure)]
        - 튜토리얼을 따라 postgresql 과 연결할 수 있는 session_maker를 작성합니다. [[Create the SQLAlchemy parts](https://fastapi.tiangolo.com/tutorial/sql-databases/?h=pydantic#create-the-sqlalchemy-parts)]
    3. `models.py` 파일을 생성합니다.
        - tablename은 `users`로 합니다.
        - 튜토리얼을 따라 postgresql 에서 사용하는 모델을 생성합니다. [[Create the database model](https://fastapi.tiangolo.com/tutorial/sql-databases/?h=pydantic#create-the-database-models)]
        
        | Column | Type | Key |
        | --- | --- | --- |
        | id | Integer | Primary, Index |
        | name | String | Unique, Index |
        | nickname | String |  |
    4. `schemas.py` 파일을 생성합니다. [[create-pydantic-models-schemas-for-reading-returning](https://fastapi.tiangolo.com/tutorial/sql-databases/?h=pydantic#create-pydantic-models-schemas-for-reading-returning)]
    5. `crud.py` 파일을 생성 후 아래 함수를 작성합니다. [[Crud Utils](https://fastapi.tiangolo.com/tutorial/sql-databases/?h=pydantic#crud-utils)]
        - `get_user`
        - `creat_user`

---
## 5. Write Dockerfile & Build Image
### 목표

- 앞서 작성한 스크립트를 실행할 수 있는 Dockerfile을 작성하고 이미지를 빌드합니다.

### 요구사항

1. 작성한 script를 build할 수 있는 dockerfile을 작성합니다.
2. 작성한 dockerfile을 이용해 이미지를 build 합니다.
3. 빌드된 이미지를 실행합니다.
4. api가 정상적으로 동작하는지 확인합니다.
