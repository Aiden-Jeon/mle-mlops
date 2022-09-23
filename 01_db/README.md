# Chapter 01) Database
---
## 1. Postgresql Server 띄우기
### 목표

- 도커를 이용해 postgres 서버를 띄워봅시다.
- `psql` 을 이용해 생성된 username과 그 역할을 확인합니다.

### 요구사항

1. Postgresql User Requirements
    - Username: `postgres`
    - Role: `Superuser`
    - Password: `mypassword`
2. Docker Run Option
    - port forwarding: 5432:5432
3. psql cli tool 을 통해 생성한 데이터 베이스에 접속합니다.
    - 다음 option을 사용해 접속합니다.
        
        `-h, --host=HOSTNAME database server host or socket directory (default: "local socket")`
        
        `-U, --username=USERNAME database user name (default: "...")`
        
4. psql 내부에서 다음 내용을 확인합니다.
    - 생성한 Role name 과 role

---
## 2. Create Table & Insert row
### 목표

- 앞서 띄운 postgres 서버에 테이블을 생성하고 row를 삽입해 봅시다.

### 요구사항

1. Python의 `psycopg2` 패키지를 이용합니다.
    - `pip install psycopg2-binary`
2. psycopg2 를 사용해 `iris_data` 이름을 가진 table을 만들어 봅시다. [[Postgres Create Table](https://www.postgresql.org/docs/current/sql-createtable.html)]
    - table은 다음과 같은 column 을 갖고 있어야 합니다.
    
    | id | sepal length (cm) | sepal width (cm) | petal length (cm) | petal width (cm) | target |
    | --- | --- | --- | --- | --- | --- |
    | serial
    (primary key) | float | float | float | float | int |
    - table을 생성할 때 아래 내용을 참고합니다.
        - 파이썬에서 표시되는 float64 는 어떻게 처리해야 할까요? [[Postgres Data Types](https://www.postgresql.org/docs/current/datatype-numeric.html)]
        - column 명은 어떻게 입력해야 할까요? [[Postgres Names](https://www.postgresql.org/docs/7.0/syntax525.htm)]
    - primary key는 어떤 역할을 하나요? 꼭 넣어야 할까요?
        - +) serial 타입은 어떤 역할을 할까요?
    - 이미 테이블이 있는데 다시 생성을 요청하면 어떻게 되나요? 어떻게 방지할 수 있을까요?
3. psycopg2 를 사용해 iris 데이터 하나를 삽입해 봅시다.
4. `psql` 등을 이용해 생성한 테이블과 삽입한 데이터를 확인합니다.

---
## 3. DB에 계속해서 데이터 삽입하기
### 목표

- postgres에 계속해서 데이터를 insert 하는 스크립트를 작성합니다.

### 요구사항

1. 앞서 작성한 스크립트를 기반으로 5초마다 iris 데이터 하나를 삽입하는 python script를 작성합니다.
2. `psql` 등을 이용해 데이터가 계속해서 삽입되고 있는지 확인합니다.

---
## 4. Write Dockerfile & Build Image
### 목표

- 앞서 작성한 스크립트를 실행할 수 있는 Dockerfile을 작성하고 이미지를 빌드합니다.

### 요구사항

1. 작성한 script를 build할 수 있는 dockerfile을 작성합니다.
2. 작성한 dockerfile을 이용해 이미지를 build 합니다.
3. 빌드된 이미지를 실행합니다.
    - 이미지가 실행될 때의 host에 대해서 생각해 봅니다.
4. `psql` 등을 이용해 DB에 데이터가 계속해서 쌓이고 있는지 확인합니다.
