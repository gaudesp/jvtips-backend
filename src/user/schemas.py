from pydantic import BaseModel, RootModel, EmailStr
from src.guide.schemas import Guide

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
  guides: list[Guide] = []
