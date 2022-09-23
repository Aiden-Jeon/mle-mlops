from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    nickname: str


class UserCreateIn(UserBase):
    pass


class UserCreateOut(UserBase):
    status: str
    id: int


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
