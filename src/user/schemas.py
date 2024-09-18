from typing import List
from pydantic import BaseModel, RootModel, EmailStr
from src.guide.schemas import Guide

class UserBase(BaseModel):
  email: EmailStr

class UserCreate(UserBase):
  password: str

class User(UserBase):
  id: int
  disabled: bool
  guides: List[Guide]

  class Config:
    from_attributes = True

class UserList(RootModel):
  root: List[User]
