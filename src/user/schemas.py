from pydantic import BaseModel, RootModel, EmailStr
from src.guide.schemas import GuidesPaginated
from src.user.models import User as UserModel
from src.pagination import Paginated, ORMNestedMixin
from typing import ClassVar

class UserBase(BaseModel):
  email: EmailStr

class UserCreate(UserBase):
  password: str

class User(UserBase):
  id: int
  disabled: bool

  class Config:
    from_attributes = True

class UsersPaginated(Paginated):
  items_model: ClassVar = User

class Users(RootModel):
  root: UsersPaginated

  class Config:
    from_attributes = True

class UserGuides(User, ORMNestedMixin):
  guides: GuidesPaginated
