from pydantic import BaseModel, RootModel
from src.guide.schemas import Guide

class GameBase(BaseModel):
  name: str

class GameCreate(GameBase):
  pass

class Game(GameBase):
  id: int

  class Config:
    from_attributes = True

class GameGuides(Game):
  guides: list[Guide] = []

class Games(RootModel):
  root: list[Game] = []
