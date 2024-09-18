from sqlalchemy.orm import Session
from src.dependencies import get_password_hash
from src.user.schemas import User, UserCreate, Users, UserGuides
from src.user.models import User as UserModel

class UserRepository:
  def __init__(self, db: Session):
    self.db = db

  def create(self, user: UserCreate) -> User:
    user = UserModel(email=user.email, hashed_password=get_password_hash(user.password))
    self.db.add(user)
    self.db.commit()
    self.db.refresh(user)
    return user
  
  def find_all(self, skip: int = 0, limit: int = 100) -> Users:
    users = self.db.query(UserModel).offset(skip).limit(limit).all()
    return users
  
  def find_one_by_id(self, user_id: int) -> User:
    user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
    return user
  
  def find_one_by_email(self, email: str) -> User:
    user = self.db.query(UserModel).filter(UserModel.email == email).first()
    return user

  def find_guides(self, user_id: int) -> UserGuides:
    user_guides = self.find_one_by_id(user_id)
    return user_guides
