from pydantic import BaseModel
from fastapi import FastAPI


KEY_VALUE_STORE = {}

app = FastAPI()


class CreateIn(BaseModel):
    name: str
    nickname: str


class CreateOut(BaseModel):
    status: str
    id: int


@app.post("/nickname", response_model=CreateOut)
def create_query(create_in: CreateIn):
    KEY_VALUE_STORE[create_in.name] = create_in.nickname
    return CreateOut(status="success", id=len(KEY_VALUE_STORE))
