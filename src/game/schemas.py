from typing import List
from pydantic import BaseModel, RootModel
from src.guide.schemas import Guide

class GameBase(BaseModel):
  name: str

class GameCreate(GameBase):
  pass

class Game(GameBase):
  id: int
  guides: List[Guide]

  class Config:
    from_attributes = True

class GameList(RootModel):
  root: List[Game]
