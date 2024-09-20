from pydantic import BaseModel, RootModel, EmailStr
from src.guide.schemas import GuidesPaginated

class UserBase(BaseModel):
  email: EmailStr

class UserCreate(UserBase):
  password: str

class User(UserBase):
  id: int
  disabled: bool

class Users(RootModel):
  root: list[User] = []

class UserGuides(User):
  guides: GuidesPaginated
  