from pydantic import BaseModel, RootModel
from src.guide.schemas import GuidesPaginated
from src.pagination import Paginated, ORMNestedMixin
from typing import ClassVar

class GameBase(BaseModel):
  name: str

class GameCreate(GameBase):
  pass

class Game(GameBase):
  id: int

  class Config:
    from_attributes = True

class GamesPaginated(Paginated):
  items_model: ClassVar = Game

class Games(RootModel):
  root: GamesPaginated

  class Config:
    from_attributes = True

class GameGuides(Game, ORMNestedMixin):
  guides: GuidesPaginated
