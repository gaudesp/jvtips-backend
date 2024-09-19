from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from src.dependencies import get_db
from src.user.schemas import User, UserCreate, Users, UserGuides
from src.user.services import UserService

router = APIRouter(tags=["users"])

@router.post("/users", response_model=User)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
  user_service = UserService(db)
  return user_service.create(data)

@router.get("/users", response_model=Users)
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  user_service = UserService(db)
  return user_service.get_all(skip, limit)

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
  user_service = UserService(db)
  user = user_service.get_by_id(user_id)
  return user

@router.get("/users/{user_id}/guides", response_model=UserGuides)
def get_game_guides(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  user_service = UserService(db)
  user_guides = user_service.get_guides(user_id, skip, limit)
  return user_guides
