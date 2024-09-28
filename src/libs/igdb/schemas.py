from typing import List
from pydantic import BaseModel

class IgdbGame(BaseModel):
  id: int
  category: int
  name: str

class IgdbGames(BaseModel):
  items: List[IgdbGame]
