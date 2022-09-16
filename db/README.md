# Postgres
## How to use
### Docker
docker cli를 통해 db를 실행시키는 방법은 다음과 같습니다.

```bash
docker run -p 5432:5432 -e POSTGRES_PASSWORD=mypassword -d postgres
```

### Docker Compose

작성되어 있는 `docker-compose.yaml`는 다음 명령어를 통해 실행할 수 있습니다.

```bash
docker-compose up -d
```
