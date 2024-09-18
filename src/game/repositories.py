from sqlalchemy.orm import Session
from src.game.schemas import Game, GameCreate, GameList
from src.game.models import Game as GameModel

class GameRepository:
  def __init__(self, db: Session):
    self.db = db

  def create(self, game: GameCreate) -> Game:
    game = GameModel(name=game.name)
    self.db.add(game)
    self.db.commit()
    self.db.refresh(game)
    return game
  
  def find_all(self, skip: int = 0, limit: int = 100) -> GameList:
    games = self.db.query(GameModel).offset(skip).limit(limit).all()
    return games
  
  def find_one_by_id(self, game_id: int) -> Game:
    game = self.db.query(GameModel).filter(GameModel.id == game_id).first()
    return game
