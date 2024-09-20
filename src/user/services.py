from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.pagination import Params
from src.user.repositories import UserRepository
from src.user.schemas import User, UserCreate, Users, UserGuides

class UserService:
  def __init__(self, db: Session):
    self.user_repository = UserRepository(db)

  def create(self, user: UserCreate) -> User:
    if self.user_repository.find_one_by_email(user.email):
      raise HTTPException(status_code=400, detail="Email already exists")
    return self.user_repository.create(user)
  
  def get_all(self, skip: int, limit: int) -> Users:
    return self.user_repository.find_all(skip, limit)
  
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

  def get_guides(self, user_id: int, params: Params) -> UserGuides:
    user = self.get_by_id(user_id)
    user_guides = self.user_repository.find_guides(user, params)
    return user_guides
