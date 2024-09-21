from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.pagination import Params
from src.game.repositories import GameRepository
from src.game.schemas import Game, GameCreate, Games, GameGuides

class GameService:
  def __init__(self, db: Session):
    self.game_repository = GameRepository(db)

  def create(self, game: GameCreate) -> Game:
    if self.game_repository.find_one_by_name(game.name):
      raise HTTPException(status_code=400, detail="Game already exists")
    return self.game_repository.create(game)
  
  def get_all(self, params: Params) -> Games:
    return self.game_repository.find_all(params)
  
  def get_by_id(self, game_id: int) -> Game:
    game = self.game_repository.find_one_by_id(game_id)
    if game is None:
      raise HTTPException(status_code=400, detail="Game not found")
    return game

  def get_guides(self, game_id: int, params: Params) -> GameGuides:
    game = self.get_by_id(game_id)
    guides = self.game_repository.find_guides(game, params)
    return guides
