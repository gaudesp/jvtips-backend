from sqlalchemy.orm import Session
from src.guide.schemas import Guide, GuideCreate, Guides
from src.guide.models import Guide as GuideModel

class GuideRepository:
  def __init__(self, db: Session):
    self.db = db

  def create(self, guide: GuideCreate, user_id: int) -> Guide:
    guide = GuideModel(**guide.model_dump(), user_id=user_id)
    self.db.add(guide)
    self.db.commit()
    self.db.refresh(guide)
    return guide
  
  def find_all(self, skip: int = 0, limit: int = 100) -> Guides:
    guides = self.db.query(GuideModel).offset(skip).limit(limit).all()
    return guides
  
  def find_one_by_id(self, guide_id: int) -> Guide:
    guide = self.db.query(GuideModel).filter(GuideModel.id == guide_id).first()
    return guide
