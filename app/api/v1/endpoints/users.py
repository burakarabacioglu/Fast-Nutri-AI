from fastapi import APIRouter, Depends, Path, HTTPException
from starlette import status
from app.models.users import User
from app.api.deps import db_dependency
from app.schemas.users import UserRegister
router = APIRouter()


@router.get("/read-all")
async def read_all(db:db_dependency):
    return db.query(User).all()

@router.get("/get_by_id/{user_id}", status_code=status.HTTP_200_OK)
async def get_by_id(db:db_dependency, user_id: int = Path(gt=0)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is not None:
        return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.post("/create-user", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRegister, db:db_dependency):
    user = User(**user.model_dump())
    db.add(user)
    db.commit()
    return user

@router.put("/update-user/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_request: UserRegister, db:db_dependency, user_id: int = Path(gt=0)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    for key,value in user_request.model_dump(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/delete-user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(db:db_dependency, user_id: int = Path(gt=0)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(db_user)
    db.commit()