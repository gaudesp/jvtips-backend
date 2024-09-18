from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.auth.services import AuthService
from src.guide.repositories import GuideRepository
from src.game.repositories import GameRepository
from src.guide.schemas import Guide, GuideCreate, GuideList

class GuideService:
  def __init__(self, db: Session, token: str = None):
    self.guide_repository = GuideRepository(db)
    self.game_repository = GameRepository(db)
    self.auth_service = AuthService(db)
    self.user_token = token

  def create(self, guide: GuideCreate) -> Guide:
    user = self.auth_service.get_current_user_by_token(self.user_token)
    game = self.game_repository.find_one_by_id(guide.game_id)
    if game is None:
      raise HTTPException(status_code=400, detail="Game not found")
    if user:
      return self.guide_repository.create(guide, user_id=user.id)
  
  def get_all(self, skip: int = 0, limit: int = 100) -> GuideList:
    return self.guide_repository.find_all(skip, limit)
  
  def get_by_id(self, guide_id) -> Guide:
    guide = self.guide_repository.find_one_by_id(guide_id)
    if guide is None:
      raise HTTPException(status_code=400, detail="Guide not found")
    return guide
