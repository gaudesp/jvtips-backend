from sqlalchemy.orm import Session
from src.pagination import paginate, Params
from src.guide.schemas import GuidesPaginated, Guides
from src.game.schemas import Game, GameCreate, Games, GamesPaginated
from src.game.models import Game as GameModel
from src.guide.models import Guide as GuideModel

class GameRepository:
  def __init__(self, db: Session):
    self.db = db

  def create(self, game: GameCreate) -> Game:
    game = GameModel(name=game.name)
    self.db.add(game)
    self.db.commit()
    self.db.refresh(game)
    return game
  
  def find_all(self, params: Params) -> Games:
    games = self.db.query(GameModel)
    paginated_games = paginate(games, params, GamesPaginated)
    return Games.model_validate(paginated_games)
  
  def find_one_by_id(self, game_id: int) -> Game:
    game = self.db.query(GameModel).filter(GameModel.id == game_id).first()
    return game
  
  def find_one_by_igdb_id(self, igdb_id: int) -> Game:
    game = self.db.query(GameModel).filter(GameModel.igdb_id == igdb_id).first()
    return game
  
  def find_one_by_name(self, name: str) -> Game:
    game = self.db.query(GameModel).filter(GameModel.name == name).first()
    return game
  
  def find_guides(self, game: Game, params: Params) -> Guides:
    guides = self.db.query(GuideModel).filter(GuideModel.game_id == game.id)
    paginated_guides = paginate(guides, params, GuidesPaginated)
    return Guides.model_validate(paginated_guides)
