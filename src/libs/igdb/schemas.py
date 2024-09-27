from typing import List
from pydantic import BaseModel

class IgbdGame(BaseModel):
  id: int
  category: int
  name: str

class IgbdGames(BaseModel):
  items: List[IgbdGame]
