from typing import List, Optional
from pydantic import BaseModel

class IgdbCover(BaseModel):
  id: int
  image_id: str

class IgdbGame(BaseModel):
  id: int
  name: str
  cover: Optional[IgdbCover] = None

class IgdbSearchGame(BaseModel):
  id: int
  category: int
  name: str
  cover: Optional[IgdbCover] = None

class IgdbSearchGames(BaseModel):
  items: List[IgdbSearchGame]
