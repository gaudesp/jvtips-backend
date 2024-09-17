from typing import List
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..domain.user import services as user_services, schemas as user_schemas

router = APIRouter(tags=["users"])

@router.post("/users", response_model=user_schemas.User)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
  db_user = user_services.get_user_by_email(db, email=user.email)
  if db_user:
    raise HTTPException(status_code=400, detail="Email already registered")
  return user_services.create_user(db=db, user=user)

@router.get("/users", response_model=List[user_schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  users = user_services.get_users(db, skip=skip, limit=limit)
  return users

@router.get("/users/{user_id}", response_model=user_schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
  db_user = user_services.get_user(db, user_id=user_id)
  if db_user is None:
    raise HTTPException(status_code=404, detail="User not found")
  return db_user
