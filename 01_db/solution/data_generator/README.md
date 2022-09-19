# Data Generator
## DB
DB 가 실행되어 있어야 합니다.
```bash
docker run -p 5432:5432 -n database -e POSTGRES_PASSWORD=mypassword -d postgres
```

## Network
DB 컨테이너와 data generator 컨테이너를 연결시키기 위한 네트워크를 생성합니다.
```bash
docker network create my-network
```

db 컨테이너를 생성한 네트워크에 연결합니다.
```bash
docker network connect my-network database
```

## Data Generator
### Build Image
이미지를 빌드합니다.

```bash
docker build --platform=linux/amd64 . -t insert_row_loop
```

### Run
docker cli를 통해 실행합니다.

```bash
docker run --network "my-network" insert_row_loop "database"
```
