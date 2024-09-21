from pydantic import BaseModel, RootModel
from src.pagination import Paginated
from typing import ClassVar

class GuideBase(BaseModel):
  title: str
  description: str
  content: str

class GuideCreate(GuideBase):
  game_id: int

class Guide(GuideBase):
  id: int
  game_id: int
  user_id: int

  class Config:
    from_attributes = True

class GuidesPaginated(Paginated):
  items_model: ClassVar = Guide

class Guides(RootModel):
  root: GuidesPaginated

  class Config:
    from_attributes = True
