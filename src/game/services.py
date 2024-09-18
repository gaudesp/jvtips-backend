from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.game.repositories import GameRepository
from src.game.schemas import Game, GameCreate, Games, GameGuides

class GameService:
  def __init__(self, db: Session):
    self.game_repository = GameRepository(db)

  def create(self, game: GameCreate) -> Game:
    if self.game_repository.find_one_by_name(game.name):
      raise HTTPException(status_code=400, detail="Game already exists")
    return self.game_repository.create(game)
  
  def get_all(self, skip: int = 0, limit: int = 100) -> Games:
    return self.game_repository.find_all(skip, limit)
  
  def get_by_id(self, game_id) -> Game:
    game = self.game_repository.find_one_by_id(game_id)
    if game is None:
      raise HTTPException(status_code=400, detail="Game not found")
    return game

  def get_guides(self, game_id) -> GameGuides:
    game = self.get_by_id(game_id)
    game_guides = self.game_repository.find_guides(game.id)
    return game_guides
