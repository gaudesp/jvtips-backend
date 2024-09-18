from typing import List
from pydantic import BaseModel, RootModel

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

class GuideList(RootModel):
  root: List[Guide]
