from pydantic import BaseModel, RootModel, EmailStr
from src.guide.schemas import GuidesPaginated
from src.user.models import User as UserModel

class UserBase(BaseModel):
  email: EmailStr

class UserCreate(UserBase):
  password: str

class User(UserBase):
  id: int
  disabled: bool

  class Config:
    from_attributes = True

class Users(RootModel):
  root: list[User] = []

class UserGuides(User):
  guides: GuidesPaginated

  @classmethod
  def from_orm_paginated(cls, user: UserModel, paginated_guides: GuidesPaginated):
    user_data = User.from_orm(user)
    
    return cls(**user_data.dict(), guides=paginated_guides)
