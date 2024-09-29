from fastapi import Depends, APIRouter, Query
from sqlalchemy.orm import Session
from src.dependencies import get_db
from src.libs.igdb.schemas import IgdbSearchGames, IgdbGame
from src.pagination import Params
from src.game.schemas import Game, GameCreate, Games
from src.game.services import GameService
from src.guide.schemas import Guides

router = APIRouter(tags=["games"])

@router.post("/games", response_model=Game)
def create_game(data: GameCreate, db: Session = Depends(get_db)):
  game_service = GameService(db)
  return game_service.create(data)

@router.get("/games", response_model=Games)
def get_games(params: Params = Depends(), db: Session = Depends(get_db)):
  game_service = GameService(db)
  return game_service.get_all(params)

@router.get("/games/search", response_model=IgdbSearchGames)
def search_games(query: str = Query(...), db: Session = Depends(get_db)):
  game_service = GameService(db)
  return game_service.search_games(query)

@router.get("/games/{igdb_id}/igdb", response_model=IgdbGame)
def get_game_data(igdb_id: int, db: Session = Depends(get_db)):
  game_service = GameService(db)
  return game_service.get_from_igdb(igdb_id)

@router.get("/games/{igdb_id}", response_model=Game)
def get_game(igdb_id: int, db: Session = Depends(get_db)):
  game_service = GameService(db)
  return game_service.get_by_igdb_id(igdb_id)

@router.get("/games/{game_id}/guides", response_model=Guides)
def get_game_guides(game_id: int, params: Params = Depends(), db: Session = Depends(get_db)):
  game_service = GameService(db)
  return game_service.get_guides(game_id, params)
