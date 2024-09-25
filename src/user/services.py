from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.pagination import Params
from src.user.repositories import UserRepository
from src.user.schemas import User, UserCreate, Users
from src.guide.schemas import Guides

class UserService:
  def __init__(self, db: Session):
    self.user_repository = UserRepository(db)

  def create(self, user: UserCreate) -> User:
    if self.user_repository.find_one_by_email(user.email):
      raise HTTPException(status_code=400, detail="Email already exists")
    return self.user_repository.create(user)
  
  def get_all(self, params: Params) -> Users:
    return self.user_repository.find_all(params)
  
  def get_by_id(self, user_id: int) -> User:
    user = self.user_repository.find_one_by_id(user_id)
    if user is None:
      raise HTTPException(status_code=400, detail="User not found")
    return user
  
  def get_by_email(self, user_id: int) -> User:
    user = self.user_repository.find_one_by_email(user_id)
    if user is None:
      raise HTTPException(status_code=400, detail="User not found")
    return user

  def get_guides(self, user_id: int, params: Params) -> Guides:
    user = self.get_by_id(user_id)
    guides = self.user_repository.find_guides(user, params)
    return guides
