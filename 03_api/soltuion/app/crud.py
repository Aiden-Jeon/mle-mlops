from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy.orm import Session

from models import User, Base
from schemas import UserCreateIn, UserCreateOut
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/user")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == user_id).first()


@app.post("/user", response_model=UserCreateOut)
def create_user(user: UserCreateIn, db: Session = Depends(get_db)):
    db_user = User(name=user.name, nickname=user.nickname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserCreateOut(name=db_user.name, nickname=db_user.nickname, status="success", id=db_user.id)
