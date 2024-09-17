from typing import List
from pydantic import BaseModel, RootModel

class UserBase(BaseModel):
  email: str

class UserCreate(UserBase):
  password: str

class User(UserBase):
  id: int
  disabled: bool

class UserList(RootModel):
  root: List[User]
