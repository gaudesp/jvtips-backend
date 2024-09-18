from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from src.dependencies import get_db
from src.game.schemas import Game, GameCreate, Games, GameGuides
from src.game.services import GameService

router = APIRouter(tags=["games"])

@router.post("/games", response_model=Game)
def create_game(data: GameCreate, db: Session = Depends(get_db)):
  game_service = GameService(db)
  return game_service.create(data)

@router.get("/games", response_model=Games)
def get_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  game_service = GameService(db)
  return game_service.get_all(skip, limit)

@router.get("/games/{game_id}", response_model=Game)
def get_game(game_id: int, db: Session = Depends(get_db)):
  game_service = GameService(db)
  game = game_service.get_by_id(game_id)
  return game

@router.get("/games/{game_id}/guides", response_model=GameGuides)
def get_game_guides(game_id: int, db: Session = Depends(get_db)):
  game_service = GameService(db)
  game_guides = game_service.get_guides(game_id)
  return game_guides
