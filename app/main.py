from fastapi import FastAPI, Depends, Path, HTTPException
from typing import Annotated

from pydantic import BaseModel, Field
from sqlalchemy import text
from starlette import status

from app.db.database import engine, SessionLocal
from app.models.users import Base, User
from sqlalchemy.orm import Session
from app.api.v1.endpoints.auth import router as auth_router


# Create the files before the app starts.
Base.metadata.create_all(engine)
app = FastAPI()
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

class UserRegister(BaseModel):
    first_name: str = Field(min_length=1, max_length=15)
    last_name: str = Field(min_length=1, max_length=30)
    email: str
    password: str
    bodyfat: float


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/read-all")
async def read_all(db:db_dependency):
    return db.query(User).all()

@app.get("/get_by_id/{user_id}", status_code=status.HTTP_200_OK)
async def get_by_id(user_id: int = Path(gt=0), db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is not None:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@app.post("/create-user", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRegister, db:db_dependency):
    user = User(**user.model_dump())
    db.add(user)
    db.commit()
    return user

@app.put("/update-user/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_request: UserRegister, db:db_dependency, user_id: int = Path(gt=0)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    for key,value in user_request.model_dump(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/delete-user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(db:db_dependency, user_id: int = Path(gt=0)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(db_user)
    db.commit()

@app.get("/healthcheck")
async def healthcheck(db: db_dependency):
    try:
        # Simply ask the DB for the number 1 to verify connection
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=503, detail="Database connection failed")
