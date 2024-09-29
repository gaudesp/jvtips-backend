from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.libs.igdb.repositories import IgdbRepository
from src.libs.igdb.schemas import IgdbSearchGames, IgdbGame
from src.pagination import Params
from src.game.repositories import GameRepository
from src.game.schemas import Game, GameCreate, Games
from src.guide.schemas import Guides

class GameService:
  def __init__(self, db: Session):
    self.game_repository = GameRepository(db)
    self.igdb_repository = IgdbRepository()

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
  
  def get_by_igdb_id(self, igdb_id: int) -> Game:
    igdb = self.game_repository.find_one_by_igdb_id(igdb_id)
    if igdb is None:
      raise HTTPException(status_code=400, detail="Game not found")
    return igdb
  
  def get_guides(self, game_id: int, params: Params) -> Guides:
    game = self.get_by_igdb_id(game_id)
    guides = self.game_repository.find_guides(game, params)
    return guides
  
  def search_games(self, query: str) -> IgdbSearchGames:
    response = self.igdb_repository.find_all(query)
    if response.status_code == 200:
      return {"items": response.json()} 
    else:
      raise HTTPException(status_code=response.status_code, detail="Error fetching data from IGDB")
    
  def get_from_igdb(self, igdb_id: int) -> IgdbGame:
    response = self.igdb_repository.find_by_igdb_id(igdb_id)
    if response.status_code == 200:
      return response.json()[0]
    else:
      raise HTTPException(status_code=response.status_code, detail="Error fetching data from IGDB")
