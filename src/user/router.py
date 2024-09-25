from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from src.dependencies import get_db
from src.pagination import Params
from src.user.schemas import User, UserCreate, Users
from src.user.services import UserService
from src.guide.schemas import Guides

router = APIRouter(tags=["users"])

@router.post("/users", response_model=User)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
  user_service = UserService(db)
  return user_service.create(data)

@router.get("/users", response_model=Users)
def get_users(params: Params = Depends(), db: Session = Depends(get_db)):
  user_service = UserService(db)
  return user_service.get_all(params)

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
  user_service = UserService(db)
  return user_service.get_by_id(user_id)

@router.get("/users/{user_id}/guides", response_model=Guides)
def get_user_guides(user_id: int, params: Params = Depends(), db: Session = Depends(get_db)):
  user_service = UserService(db)
  return user_service.get_guides(user_id, params)
