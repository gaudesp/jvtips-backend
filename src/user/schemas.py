from typing import List
from pydantic import BaseModel, RootModel, EmailStr

class UserBase(BaseModel):
  email: EmailStr

class UserCreate(UserBase):
  password: str

class User(UserBase):
  id: int
  disabled: bool

class UserList(RootModel):
  root: List[User]
