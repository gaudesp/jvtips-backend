from sqlalchemy.orm import Session
from app.src.dependencies import get_password_hash
from app.src.user.schemas import User, UserCreate, UserList
from app.src.user.models import User as user_model

class UserRepository:
  def __init__(self, db: Session):
    self.db = db

  def create(self, user: UserCreate) -> User:
    user = user_model(email=user.email, hashed_password=get_password_hash(user.password))
    self.db.add(user)
    self.db.commit()
    self.db.refresh(user)
    return user
  
  def find_all(self, skip: int = 0, limit: int = 100) -> UserList:
    users = self.db.query(user_model).offset(skip).limit(limit).all()
    return users
  
  def find_one_by_id(self, user_id: int) -> User:
    user = self.db.query(user_model).filter(user_model.id == user_id).first()
    return user
  
  def find_one_by_email(self, email: str) -> User:
    user = self.db.query(user_model).filter(user_model.email == email).first()
    return user
