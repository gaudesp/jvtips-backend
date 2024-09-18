from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.game.repositories import GameRepository
from src.game.schemas import Game, GameCreate, GameList

class GameService:
  def __init__(self, db: Session):
    self.game_repository = GameRepository(db)

  def create(self, game: GameCreate) -> Game:
    return self.game_repository.create(game)
  
  def get_all(self, skip: int = 0, limit: int = 100) -> GameList:
    return self.game_repository.find_all(skip, limit)
  
  def get_by_id(self, game_id) -> Game:
    game = self.game_repository.find_one_by_id(game_id)
    if game is None:
      raise HTTPException(status_code=400, detail="Game not found")
    return game
