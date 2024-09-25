from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.pagination import Params
from src.auth.services import AuthService
from src.guide.repositories import GuideRepository
from src.game.services import GameService
from src.guide.schemas import Guide, GuideCreate, Guides

class GuideService:
  def __init__(self, db: Session, token: str = None):
    self.guide_repository = GuideRepository(db)
    self.game_service = GameService(db)
    self.auth_service = AuthService(db)
    self.user_token = token

  def create(self, guide: GuideCreate) -> Guide:
    user = self.auth_service.get_current_user(self.user_token)
    game = self.game_service.get_by_id(guide.game_id)
    return self.guide_repository.create(guide, user_id=user.id, game_id=game.id)
  
  def get_all(self, params: Params) -> Guides:
    return self.guide_repository.find_all(params)
  
  def get_by_id(self, guide_id) -> Guide:
    guide = self.guide_repository.find_one_by_id(guide_id)
    if guide is None:
      raise HTTPException(status_code=400, detail="Guide not found")
    return guide
